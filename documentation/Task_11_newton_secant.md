# Task 11: Root Finding — Newton-Raphson and Secant Methods

## 1. Problem Description

This task applies Newton–Raphson and the Secant method to calculate the Internal Rate of Return (IRR) of an investment using its initial cost and future annual cash inflows.

## 2. Input Values

The original cash flows are:

`[-10000, 3000, 3500, 4000, 2500]`

The first value represents the initial investment, while the remaining values represent annual cash inflows.

## 3. Mathematical Operations

The program defines a Net Present Value (NPV) function and its derivative. Newton–Raphson uses the derivative to estimate the root, while the Secant method uses two initial estimates to approximate the slope.

Both methods use SciPy's `root_scalar` function to find the rate at which NPV equals zero.

## 4. Original Results

Both methods calculated an IRR of approximately 11.542461%. The NPV at the Newton–Raphson solution was approximately zero, indicating that the calculated rate solves the NPV equation.

## 5. Parameter Change and Interpretation

The initial investment was increased from 10,000 to 12,000, while the future cash inflows remained unchanged.

Both methods then calculated an IRR of approximately 3.329828%. The decrease in IRR demonstrates that a higher initial cost reduces the return rate when future cash inflows remain constant.

## 6. Real-World Application

Root-finding methods can be used in financial analysis to calculate the IRR of investments. Newton–Raphson is useful when the derivative of the NPV function is available, while the Secant method can be applied without explicitly providing the derivative.

## 7. Conclusion

Newton–Raphson and the Secant method produced matching IRR results for both investment scenarios. Increasing the initial investment reduced the calculated IRR from approximately 11.54% to 3.33%.