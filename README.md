# Interactive 2D Lyapunov Function Demo

This repository contains a Python demonstration for **visualizing candidate Lyapunov functions and their derivatives** in a 2D system. It is fully interactive and allows you to explore the stability of equilibrium points using visual tools.

---

## **Files**

- `interactive_lyapunov_2D.py` : Main Python script containing the interactive Lyapunov function demo.
- `README.md` : This documentation file.

---

## **Description**

Description

This demo performs the following tasks:

Lyapunov Analysis

Checks if a candidate function V(x1, x2) can be used as a Lyapunov function for a given system with dynamics:

x1_dot = f1(x1, x2)

x2_dot = f2(x1, x2)

The following conditions are verified:

V(0,0) = 0 at the equilibrium point.

V(x1, x2) > 0 for all points other than the equilibrium (positive definite).

The derivative along the system trajectory, Vdot(x1, x2) = dV/dt, is less than or equal to 0 everywhere (non-increasing along the system motion).

The program reports the stability type and gives a conclusion about whether the candidate function is valid.

Interactive Visualization

3D surface plot of V(x1, x2) or Vdot(x1, x2) over a 2D grid.

Adjustable Z-slice slider to inspect contour levels.

Textbox to enter a specific Z value for the contour line.

Radio buttons to switch between viewing V and Vdot.

Plane orientation buttons to change the viewing angle:

x1-x2 plane

x1-z plane

x2-z plane

---

## **Dependencies**

Make sure you have the following Python packages installed:

- `numpy`
- `sympy`
- `matplotlib`

You can install them using `pip`:

```bash
pip install numpy sympy matplotlib
