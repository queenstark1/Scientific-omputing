# Task 7: Gaussian Elimination and LU Decomposition

## 1. Objective
To solve multiple systems of linear equations by reusing an LU factorization of the same coefficient matrix.

## 2. Input Values
The coefficient matrix is:

A = [[4, -1, 0], [-1, 4, -1], [0, -1, 3]]

The original measurement vectors are [15, 10, 10], [16, 11, 9], and [14, 12, 11].

## 3. Mathematical Operations
The program uses `lu_factor(A)` to factor the coefficient matrix once. It then uses `lu_solve((lu, piv), b)` to solve each measurement system. Residual norms measure the difference between the given measurements and the reconstructed results. The first solution is also checked using `np.linalg.solve()`.

## 4. Initial Results
For measurement set 1, the solution was [5, 5, 5]. Measurement set 2 produced approximately [5.317, 5.268, 4.756], while measurement set 3 produced approximately [4.902, 5.610, 5.537]. The residual norms were zero or extremely close to zero. The direct solution for the first set agreed with the LU solution.

## 5. Parameter Change
The first value in measurement set 1 was changed from 15 to 18, making the vector [18, 10, 10].

The new solution was approximately [5.805, 5.220, 5.073]. The solutions for measurement sets 2 and 3 remained unchanged because their inputs did not change. The direct solution for the modified first set matched the LU solution.

## 6. Interpretation
Changing a measurement value changes the solution for that measurement set. Reusing the LU factors allows the program to solve new systems without factoring the same coefficient matrix again. The small residual values indicate that the solutions satisfy the equations within numerical precision.

## 7. Related Real-World Application
This method is useful in engineering simulations or monitoring systems where the same mathematical model is used repeatedly with new measurements. Reusing the factorization can reduce repeated computation.

## 8. Conclusion
LU decomposition provides a reusable way to solve multiple linear systems with the same coefficient matrix. Comparing the result with a direct solution and checking the residuals help verify correctness.