#!/usr/bin/env python3
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, TextBox, Button

# ==============================
# Core Lyapunov analysis function
# ==============================
def is_lyapunov(f_str, V_str, domain_limit=3.0, num_points=40):
    """
    Returns: (passed_boolean, report_string, V_sympy, Vdot_sympy, stability_type)
    """
    x1, x2 = sp.symbols('x1 x2')
    x = sp.Matrix([x1, x2])

    # Parse functions
    f = sp.Matrix([sp.sympify(fi) for fi in f_str])
    V = sp.sympify(V_str)
    report_lines = []

    # --- Condition 1: V(0) = 0 ---
    V0 = V.subs({x1: 0, x2: 0})
    cond1_pass = (V0 == 0)
    report_lines.append(
        f"Condition 1: V(0)=0 ---> {'PASS' if cond1_pass else 'FAIL'}"
    )

    # --- Condition 2: V(x) > 0 for x != 0 ---
    lin = np.linspace(-domain_limit, domain_limit, num_points)
    Xg, Yg = np.meshgrid(lin, lin)
    grid = np.vstack([Xg.ravel(), Yg.ravel()]).T
    non_origin = np.linalg.norm(grid, axis=1) > 1e-8

    V_func = sp.lambdify((x1, x2), V, 'numpy')
    V_vals = np.array(V_func(grid[:,0], grid[:,1]), dtype=float).ravel()
    cond2_pass = np.all(V_vals[non_origin] > 0)
    report_lines.append(
        f"Condition 2: V(x)>0 for x!=0 ---> {'PASS' if cond2_pass else 'FAIL'}"
    )

    # --- Condition 3: Vdot ---
    grad_V = sp.Matrix([sp.diff(V, var) for var in x])
    Vdot = sp.simplify(grad_V.dot(f))

    # Numeric check
    Vdot_func = sp.lambdify((x1, x2), Vdot, 'numpy')
    Vdot_vals = np.array(Vdot_func(grid[:, 0], grid[:, 1]), dtype=float).ravel()

    if np.any(Vdot_vals[non_origin] > 1e-8):
        cond3_text = "Vdot(x) > 0 somewhere"
        stability_type = "Inconclusive"
        cond3_pass = "FAIL"
    else:
        cond3_text = "Vdot(x) <= 0 everywhere on grid"
        stability_type = "Stable equilibrium (Check the interactive display for the type.)"
        cond3_pass = "PASS"

    report_lines.append(f"Vdot(x) : {Vdot}")
    report_lines.append(f"Condition 3: {cond3_text} ---> {cond3_pass}")
    report_lines.append(f"Stability: {stability_type}")

    # --- Final PASS logic ---
    final_pass = cond1_pass and cond2_pass and (cond3_pass == "PASS")

    if final_pass:
        report_lines.append("\nConclusion: This function can be used as a Lyapunov function.")
    else:
        report_lines.append("\nConclusion: This function cannot be used as a Lyapunov function, pick a new candidate.")

    return final_pass, "\n".join(report_lines), V, Vdot, stability_type

# ==============================
# Interactive plotting function
# ==============================
def interactive_lyapunov(f1_str, f2_str, V_str):
    # --- Run Lyapunov analysis ---
    passed, report, V, Vdot, stability = is_lyapunov([f1_str, f2_str], V_str)
    print(report)

    # --- Numeric grid ---
    x1, x2 = sp.symbols("x1 x2")
    N = 80
    lim = 3
    X = np.linspace(-lim, lim, N)
    Y = np.linspace(-lim, lim, N)
    Xg, Yg = np.meshgrid(X, Y)
    V_func = sp.lambdify((x1, x2), V, "numpy")
    Vdot_func = sp.lambdify((x1, x2), Vdot, "numpy")
    Z_V = V_func(Xg, Yg)
    Z_Vdot = Vdot_func(Xg, Yg)

    # --- Matplotlib interactive figure ---
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    plt.subplots_adjust(left=0.25, right=0.95, bottom=0.2)

    current_surface = 0  # 0=V, 1=Vdot
    slider = None
    textbox = None

    # Helper functions
    def get_current_Z():
        return Z_V if current_surface == 0 else Z_Vdot

    def get_current_title():
        return "V(x)" if current_surface == 0 else "Vdot(x)"

    def update_surface(val):
        nonlocal slider, textbox
        ax.clear()
        Z = get_current_Z()
        cmap = 'viridis' if current_surface == 0 else 'plasma'
        title = get_current_title()
        z_val = slider.val
        ax.plot_surface(Xg, Yg, Z, cmap=cmap, alpha=0.7)
        ax.contour(Xg, Yg, Z, levels=[z_val], colors='red', linestyles='dashed', offset=z_val)
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('Value')
        ax.set_title(title)
        fig.canvas.draw_idle()
        if textbox:
            textbox.set_val(f"{z_val:.3f}")

    def slider_update(val):
        update_surface(val)

    def textbox_update(text):
        nonlocal slider
        try:
            val = float(text)
            Z = get_current_Z()
            val = np.clip(val, Z.min(), Z.max())
            slider.set_val(val)
        except ValueError:
            pass

    def switch_surface(label):
        nonlocal current_surface, slider, textbox
        current_surface = 0 if label == 'V(x)' else 1
        Z = get_current_Z()

        slider.ax.clear()
        slider_valinit = Z.min() if current_surface == 0 else Z.max()
        slider_new = Slider(slider.ax, 'Z-slice', Z.min(), Z.max(),
                            valinit=slider_valinit, orientation='vertical')
        slider_new.on_changed(slider_update)
        slider = slider_new

        textbox.ax.clear()
        textbox_new = TextBox(textbox.ax, 'Z value', initial=f"{slider_valinit:.3f}")
        textbox_new.on_submit(textbox_update)
        textbox = textbox_new

        update_surface(None)

    # --- Slider ---
    ax_slider = plt.axes([0.2, 0.25, 0.03, 0.65])
    slider = Slider(ax_slider, 'Z-slice', Z_V.min(), Z_V.max(),
                    valinit=Z_V.min(), orientation='vertical')
    slider.on_changed(slider_update)

    # --- Textbox below figure ---
    ax_text = plt.axes([0.5, 0.1, 0.05, 0.04])
    textbox = TextBox(ax_text, 'Z value', initial=f"{Z_V.min():.3f}")
    textbox.on_submit(textbox_update)

    # --- Radio buttons ---
    ax_radio = plt.axes([0.25, 0.5, 0.1, 0.15])
    radio = RadioButtons(ax_radio, ('V(x)', 'Vdot(x)'))
    radio.on_clicked(switch_surface)

    # --- Buttons for orientation ---
    ax_btn1 = plt.axes([0.08, 0.8, 0.1, 0.05])
    ax_btn2 = plt.axes([0.08, 0.55, 0.1, 0.05])
    ax_btn3 = plt.axes([0.08, 0.3, 0.1, 0.05])
    btn_x1x2 = Button(ax_btn1, "x1-x2 plane")
    btn_x1z  = Button(ax_btn2, "x1-z plane")
    btn_x2z  = Button(ax_btn3, "x2-z plane")

    def set_view_x1x2(event):
        ax.view_init(elev=90, azim=-90)
    def set_view_x1z(event):
        ax.view_init(elev=0, azim=-90)
    def set_view_x2z(event):
        ax.view_init(elev=0, azim=0)

    btn_x1x2.on_clicked(set_view_x1x2)
    btn_x1z.on_clicked(set_view_x1z)
    btn_x2z.on_clicked(set_view_x2z)

    # --- Initial plot ---
    update_surface(None)
    plt.show()

# ==============================
# Example usage
# ==============================
if __name__ == "__main__":
    x1, x2 = sp.symbols("x1 x2")

    # --- input dynamics ---
    x1dot = -x1**3
    x2dot = -x2

    # --- candidate Lyapunov ---
    V = x1**2 + x2**2

    interactive_lyapunov(f1_str=str(x1dot), f2_str=str(x2dot), V_str=str(V))
