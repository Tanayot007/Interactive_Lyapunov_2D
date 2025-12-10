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

1. Test whether a candidate function V(x1, x2) is a Lyapunov function for a given 2D dynamical system:
   dx1/dt = f1(x1, x2)
   dx2/dt = f2(x1, x2)
2. Explore the stability of the system visually through 3D plots.
3. Interactively inspect surfaces and contours of V(x1, x2) and d/dtV(x1, x2).

---

## **Technical Analysis**

The demo performs the following steps:

1. **Lyapunov Analysis**
   - Condition 1: V(0,0) = 0 at the equilibrium point.
   - Condition 2: V(x1, x2) > 0 for all (x1, x2) - {(0,0)} (positive definite).
   - Condition 3: dV/dt <= 0 for all (x1, x2) - {(0,0)} (non-increasing along system trajectories).
   - Based on these conditions, the program determines:
     - If the candidate function is a valid Lyapunov function.
     - The type of stability (stable/inconclusive).
   Note: In theory
      1. if dV/dt <= 0 (negative semidefinite), we can say this equilibrium point is Lyapunov stable.
      2. if dV/dt < 0 (negative definite), we can say this equilibrium point is Asymtotically stable.
      However, it is not easy to check numerically, so I have the interactive functions ready, following the python file.

2. **Interpretation of Results**
   - If `V(x)` satisfies all three conditions, the candidate Lyapunov function can be used to determine system stability and the system is **stable** around the equilibrium.
   - If one of the conditions fails, the candidate function is **not valid**, and the stability is inconclusive.
   - Users can explore the numeric and visual behavior to understand how trajectories would evolve.
   - In theory, the user can visualize the displayed functions and interact with them to determine the stability type (asymptotically stable or Lyapunov stable). If the user cannot find any point where dV/dt = 0 in the region of interest, excluding the origin—that is, in (x1, x2) - {(0,0)}—then the system is asymptotically stable; otherwise, it is only Lyapunov stable. However, the numerical calculation in this code should not be the reference for determining if the system is Lyapunov stable or asymptotically stable.

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

Test case 1: x1dot= -x1, x2dot=-2*x2, V(candidate Lyapunov function)=x1^2 + x2^2

![sample_output1](https://github.com/Tanayot007/Interactive_Lyapunov_2D/blob/main/1.png)

![Vdot(x) surface](https://github.com/Tanayot007/Interactive_Lyapunov_2D/blob/main/2.png)

Conclusion: This candidate Lyapunov function can be used to determine the system stability

Test case 2: x1dot= -x1, x2dot=-2*x2, V(candidate Lyapunov function)=x1^2 - x2^2

![sample_output1](https://github.com/Tanayot007/Interactive_Lyapunov_2D/blob/main/3.png)

![Vdot(x) surface](https://github.com/Tanayot007/Interactive_Lyapunov_2D/blob/main/4.png)

Conclusion: This candidate Lyapunov function cannot be used to determine the system stability. User need to pick a new one.
Reasons: The candidate does not obey condition 2 and 3.


---

## **Dependencies**

You need Python 3 and the following packages:

- `numpy`
- `sympy`
- `matplotlib`

Install them using pip:

```bash
pip install numpy sympy matplotlib
