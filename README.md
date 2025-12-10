# Interactive 2D Lyapunov Function Demo

This repository contains a Python demonstration for **visualizing candidate Lyapunov functions and their derivatives** in a 2D system. It is fully interactive and allows you to explore the stability of equilibrium points using visual tools.

---

## **Files**

- `interactive_lyapunov_2D.py` : Main Python script containing the interactive Lyapunov function demo.
- `README.md` : This documentation file.
- `images/` : (Optional) Folder to store screenshots of the demo.

---

## **Overview**

This demo allows users to:

1. Test whether a candidate function \(V(x_1, x_2)\) is a Lyapunov function for a given 2D dynamical system:
   \[
   \dot{x}_1 = f_1(x_1, x_2), \quad
   \dot{x}_2 = f_2(x_1, x_2)
   \]
2. Explore the stability of the system visually through 3D plots.
3. Interactively inspect surfaces and contours of \(V(x)\) and \(\dot{V}(x)\).

---

## **Technical Analysis**

The demo performs the following steps:

1. **Lyapunov Analysis**
   - Condition 1: \(V(0) = 0\) at the equilibrium point.
   - Condition 2: \(V(x) > 0\) for all \(x \neq 0\) (positive definite).
   - Condition 3: \(\dot{V}(x) \le 0\) for all \(x \neq 0\) (non-increasing along system trajectories).
   - Based on these conditions, the program determines:
     - If the candidate function is a valid Lyapunov function.
     - The type of stability (stable/inconclusive).

2. **Interpretation of Results**
   - If `V(x)` satisfies all three conditions, the system is **stable** around the equilibrium.
   - If `Vdot(x) > 0` anywhere, the candidate function is **not valid**, and the system may be unstable or inconclusive.
   - Users can explore the numeric and visual behavior to understand how trajectories would evolve.

---

## **Interactive Visualization**

- **3D Surface Plot**
  - Visualizes `V(x)` or `Vdot(x)` over a 2D grid.
  - Use mouse to rotate, zoom, and pan.
  
- **Slider**
  - Adjusts a Z-slice to inspect contour lines.

- **Textbox**
  - Enter a specific Z value to highlight contour lines at that height.

- **Radio Buttons**
  - Switch between viewing `V(x)` or `Vdot(x)`.

- **Plane Orientation Buttons**
  - x1-x2 plane
  - x1-z plane
  - x2-z plane

---

## **Example Screenshots**

*(Replace these with your own screenshots in `images/` folder.)*

![V(x) surface](images/V_surface.png)

![Vdot(x) surface](images/Vdot_surface.png)

---

## **Dependencies**

You need Python 3 and the following packages:

- `numpy`
- `sympy`
- `matplotlib`

Install them using pip:

```bash
pip install numpy sympy matplotlib
