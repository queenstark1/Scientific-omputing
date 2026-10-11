# Task 4: Floating-Point Arithmetic and Numerical Errors

## 1. Mathematical Concept

Computers store real numbers using a finite number of binary digits. Consequently, some decimal values are represented approximately. Absolute error measures the difference between the true and approximate values, while relative error expresses the absolute error in relation to the true value. Round-off error arises from finite computer precision, whereas truncation error arises when an exact mathematical process is replaced by an approximation.

## 2. Real-World Problem

A scientific computing program must compare decimal values, calculate numerical approximations and minimize errors when performing calculations. Incorrect assumptions about floating-point equality can cause problems in scientific simulations, engineering and navigation.

## 3. Input Data

The program uses 0.1, 0.2 and 0.3 to demonstrate floating-point comparison. It also compares the true value of √2 with the approximation 1.414 and evaluates two mathematically equivalent formulas for x = 10⁻⁴, 10⁻⁸ and 10⁻¹².

## 4. Mathematical Operations

The program performs an exact equality comparison and a tolerance-based comparison using `np.isclose()`. It calculates absolute error as the absolute difference between the true and approximate values, and relative error as the absolute error divided by the absolute true value. Finally, it compares a direct formula with a numerically more stable equivalent formula.

## 5. Implementation

The program is saved as `code/Task_04_numerical_errors.py`. It uses NumPy for square-root calculations and tolerance-based comparisons.

## 6. Results and Interpretation

The expression 0.1 + 0.2 produced 0.30000000000000004. The exact comparison with 0.3 returned False, while `np.isclose()` returned True.

The absolute error for approximating √2 as 1.414 was 0.00021356, and the relative error was approximately 0.01510114%.

The direct and stable formulas produced increasingly different results as x became smaller. At x = 10⁻¹², the direct formula produced approximately 0.500044450291, while the stable formula produced 0.500000000000. This demonstrates the effect of numerical instability caused by subtracting nearly equal numbers.

## 7. Parameter Modification and Comparison

**Change made:** The value of x was evaluated at three different magnitudes: 10⁻⁴, 10⁻⁸ and 10⁻¹².

**Results:** As x decreased, the direct formula became less accurate relative to the stable formula. At 10⁻⁴ the results were almost identical, while at 10⁻¹² the difference became more noticeable.

**Interpretation:** Changing x demonstrated that numerical accuracy depends on the formulation of a calculation. The stable formula was more reliable for very small values of x.

## 8. Related Real-World Application

These methods can be applied in engineering simulations and navigation systems, where numerical errors can affect calculated positions, measurements or predictions. Tolerance-based comparisons and numerically stable formulas help reduce errors in such calculations.

## 9. Conclusion

The experiment demonstrated that floating-point values may not be represented exactly, that absolute and relative errors measure approximation accuracy, and that mathematically equivalent formulas can differ in numerical stability.