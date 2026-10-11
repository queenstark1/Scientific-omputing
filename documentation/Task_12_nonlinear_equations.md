# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Problem Description

This task uses SciPy to find the intersection points of a circle and a parabola by solving a system of two nonlinear equations.

The equations are:

- Circle: \(x^2+y^2=4\)
- Parabola: \(y=x^2-1\)

## 2. Input Values

The program uses two initial guesses: \([1.0,1.0]\) and \([-1.0,1.0]\). The modified experiment changes the second guess to \([-2.0,1.5]\).

## 3. Mathematical Operations

The `equations()` function returns the residuals of the circle and parabola equations. SciPy's `root()` function estimates the values of \(x\) and \(y\) that make both residuals zero.

## 4. Original Results

Using the initial guesses \([1.0,1.0]\) and \([-1.0,1.0]\), the program found two intersections:

- \((1.51748991,1.30277564)\)
- \((-1.51748991,1.30277564)\)

Both solutions converged successfully, and their residuals were approximately \(10^{-13}\), indicating that the equations were satisfied to high numerical precision.

## 5. Parameter Change and Interpretation

The second initial guess was changed from \([-1.0,1.0]\) to \([-2.0,1.5]\). The solver still found the left intersection, approximately \((-1.51748991,1.30277564)\).

This demonstrates that different initial guesses can lead a nonlinear solver toward different solutions. However, the modified guess did not change the final intersection in this experiment.

## 6. Real-World Application

Nonlinear equation-solving methods can be used to find geometric intersections, solve engineering models, calibrate systems and determine operating points in control systems.

## 7. Conclusion

The SciPy `root()` function successfully found both intersections of the circle and parabola. The residuals were close to zero, confirming the accuracy of the calculated solutions. Changing the initial guess provided an opportunity to observe how starting values affect nonlinear solving.

