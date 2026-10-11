# Task 10: Root Finding — Bisection and Fixed-Point Methods

## 1. Problem Description

This task applies the bisection and fixed-point methods to determine the equilibrium temperature of a simplified nonlinear heat-balance model. Equilibrium occurs when the heat-balance function equals zero.

## 2. Input Values

The original heat-balance equation is:

\(f(T)=T-25-10e^{-T/20}\)

The bisection method uses the interval [20, 40], while fixed-point iteration starts with an initial temperature of 30°C. Both methods use a tolerance of \(10^{-10}\).

## 3. Mathematical Operations

The bisection method repeatedly halves an interval containing a root. The fixed-point method rewrites the equation as:

\(T=25+10e^{-T/20}\)

The program uses SciPy's `root_scalar` for bisection and repeated substitution for fixed-point iteration. It also plots the heat-balance function and marks the equilibrium temperature.

## 4. Original Results

The bisection method found an equilibrium temperature of 27.525211°C. Fixed-point iteration produced the same temperature to six decimal places and required 13 iterations.

## 5. Parameter Change and Interpretation

The coefficient in the exponential term was changed from 10 to 15 in both the heat-balance and fixed-point functions.

The modified equilibrium temperature was 28.591212°C, and fixed-point iteration required 15 iterations. The equilibrium temperature increased by approximately 1.066°C because the change in the model altered the balance represented by the equation.

## 6. Graph Interpretation

The graph is saved as `plots/Task_10_equilibrium_temperature.png`. It displays the heat-balance function over temperatures from 20°C to 40°C. The equilibrium temperature is identified where the function crosses the horizontal zero line.

## 7. Real-World Application

Root-finding methods can be used to solve engineering equations, determine physical equilibrium points, calibrate systems and calculate thresholds. In this example, the methods estimate the temperature at which a heat-balance equation becomes zero.

## 8. Conclusion

Both bisection and fixed-point iteration successfully found the equilibrium temperature. Increasing the model coefficient from 10 to 15 raised the calculated equilibrium temperature from 27.525211°C to 28.591212°C.