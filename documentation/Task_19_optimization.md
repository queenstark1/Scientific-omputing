# Task 19: Numerical Optimization

## Objective
To use SciPy's `minimize` function to find a low-cost allocation of two server types while satisfying a minimum processing-capacity requirement.

## Method
The objective function was:

\[
C=12x+18y
\]

where \(x\) and \(y\) represent the allocations of Type A and Type B servers. Their respective capacities were 100 and 170 units. The optimization used the SLSQP method, non-negative bounds, and a minimum-capacity constraint.

A separate integer search was used to identify a low-cost solution using whole servers.

## Results
Initially, with a minimum capacity of 1,000 units, the continuous solution allocated 0 Type A units and approximately 5.882 Type B units. It achieved a capacity of 1,000 units at a cost of 105.88. The best whole-server solution was 0 Type A and 6 Type B servers, providing 1,020 units at a cost of 108.

The capacity requirement was then increased to 1,200 units. The continuous solution allocated approximately 7.059 Type B units, achieving a cost of 127.06. The integer search was updated to use the same 1,200-unit requirement.

## Discussion
The experiment demonstrates that increasing the required capacity increases the minimum cost. Continuous optimization can produce fractional allocations, whereas the integer search considers whole-server combinations. Both methods must use the same capacity requirement for a fair comparison.

## Conclusion
SciPy optimization can minimize an objective function while satisfying constraints. Integer searches are useful when the solution must represent whole servers rather than fractional units.