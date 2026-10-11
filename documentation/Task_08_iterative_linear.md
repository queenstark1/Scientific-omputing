# Task 8: Iterative Methods for Linear Systems

## 1. Problem Description

This task applies the Jacobi and Gauss-Seidel iterative methods to a simplified steady-state temperature model consisting of five interior grid points. The aim is to estimate the temperature at each point using the influence of the boundary temperatures.

## 2. Input Values

The coefficient matrix represents relationships between neighboring grid points. The vector \(b\) represents the boundary influence, with a left boundary temperature of 100°C and a right boundary temperature of 20°C.

## 3. Mathematical Operations

The program solves the linear system \(Ax=b\) using the Jacobi and Gauss-Seidel methods. It also uses NumPy's `np.linalg.solve()` to calculate a direct solution for comparison. The stopping tolerance for both iterative methods is set to \(10^{-4}\).

## 4. Results

- Jacobi iterations: 86
- Gauss-Seidel iterations: 43
- Approximate temperatures from Jacobi: 86.6665°C, 73.3331°C, 59.9997°C, 46.6664°C and 33.3332°C.
- Approximate temperatures from Gauss-Seidel: 86.6665°C, 73.3330°C, 59.9997°C, 46.6665°C and 33.3332°C.
- Direct solution: approximately 86.6667°C, 73.3333°C, 60.0000°C, 46.6667°C and 33.3333°C.

## 5. Parameter Change and Interpretation

The tolerance was changed to \(10^{-4}\) for both methods. The methods stop when the maximum change between successive estimates falls below this threshold. The results show that Gauss-Seidel required 43 iterations, compared with 86 for Jacobi. Therefore, Gauss-Seidel converged in fewer iterations for this system.

## 6. Graph Interpretation

The convergence graph is saved as `plots/Task_08_convergence.png`. It plots the maximum change between successive estimates against the iteration number using a logarithmic vertical axis. A decreasing curve indicates convergence toward a stable solution.

## 7. Related Real-World Application

These methods can be used to estimate steady-state temperature distributions in heat-transfer models. Similar numerical approaches are useful when a physical system is divided into grid points and the unknown values at those points must be estimated.

## 8. Conclusion

Both iterative methods produced temperatures close to the direct solution. Gauss-Seidel required fewer iterations than Jacobi for this example, demonstrating its faster convergence in this particular system.