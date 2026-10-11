# Task 6: Solution of Systems of Linear Equations

## 1. Objective
To solve simultaneous linear equations using NumPy and estimate the number of two types of servers from their CPU and memory usage.

## 2. Input Values
Type A servers use 4 CPU units and 8 GB of memory each. Type B servers use 2 CPU units and 12 GB of memory each. Initially, the total resource usage is 20 CPU units and 72 GB of memory.

## 3. Mathematical Operations
The problem is represented as Ax = b, where A contains the coefficients, x contains the unknown server counts, and b contains the known resource totals. The function `np.linalg.solve(A, b)` calculates the solution. Matrix multiplication and residual calculations verify the result.

## 4. Initial Results
The program calculated 3 Type A servers and 4 Type B servers. Verification returned [20, 72], matching the original resource totals. The residual norm was 0.0.

## 5. Parameter Change
The total CPU usage was increased from 20 to 24 units while memory usage remained at 72 GB.

The modified solution was 4 Type A servers and 3 Type B servers. Verification returned [24, 72], and the residual norm remained 0.0.

## 6. Interpretation
Changing the CPU total changed the combination of server types that satisfies both resource equations. The verification results confirm that the calculated values satisfy the specified totals.

## 7. Related Real-World Application
This approach can help estimate quantities of different server types from known CPU and memory usage. Similar systems of equations are used in electrical circuit analysis, resource allocation and traffic-flow models.

## 8. Conclusion
NumPy can solve systems of linear equations efficiently. Verifying the solution with matrix multiplication and residuals helps confirm that the calculated values satisfy the original equations.