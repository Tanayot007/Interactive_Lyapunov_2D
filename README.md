# Interactive 2D Lyapunov Function Demo

This repository contains a Python demonstration for **visualizing candidate Lyapunov functions and their derivatives** in a 2D system. It is fully interactive and allows you to explore the stability of equilibrium points using visual tools.

---

## **Files**

- `interactive_lyapunov_2D.py` : Main Python script containing the interactive Lyapunov function demo.
- `README.md` : This documentation file.

---

## **Description**

This demo performs the following tasks:

1. **Lyapunov Analysis**
   - Checks if a candidate function \(V(x_1, x_2)\) is a Lyapunov function for the given system:
     \[
     \dot{x}_1 = f_1(x_1, x_2), \quad
     \dot{x}_2 = f_2(x_1, x_2)
     \]
   - Conditions checked:
     1. \(V(0) = 0\) at the equilibrium.
     2. \(V(x) > 0\) for all \(x \neq 0\) (positive definite).
     3. \(\dot{V}(x) \le 0\) for all \(x \neq 0\) (non-increasing along system trajectories).
   - Reports the stability type and gives a conclusion if the candidate function can be used.

2. **Interactive Visualization**
   - 3D surface plot of \(V(x)\) or \(\dot{V}(x)\) over a 2D domain.
   - Adjustable **Z-slice** slider to inspect contours.
   - **Textbox** to enter a specific Z value for contour lines.
   - **Radio buttons** to switch between viewing \(V(x)\) and \(\dot{V}(x)\).
   - **Plane orientation buttons**:
     - x1-x2 plane
     - x1-z plane
     - x2-z plane

---

## **Dependencies**

Make sure you have the following Python packages installed:

- `numpy`
- `sympy`
- `matplotlib`

You can install them using `pip`:

```bash
pip install numpy sympy matplotlib
