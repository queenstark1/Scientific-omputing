# Task 18: Numerical Solution of ODEs Using SciPy

## Objective
To solve an ordinary differential equation using SciPy's `solve_ivp` and compare the numerical solution with the exact solution of an RC charging circuit.

## Method
The circuit is modelled using the differential equation:

\[
\frac{dV}{dt}=\frac{V_s-V}{RC}
\]

The supply voltage was 5 V, the resistance was initially 1000 Ω, and the capacitance was 0.001 F. The initial capacitor voltage was 0 V. SciPy's `solve_ivp` was used to calculate the voltage over five seconds. The numerical result was compared with the exact solution.

## Results
With a resistance of 1000 Ω, the capacitor voltage after five seconds was 4.9663 V. The maximum error against the exact solution was \(9.282\times10^{-10}\) V.

The resistance was then increased to 2000 Ω while the other parameters remained unchanged. The voltage after five seconds decreased to 4.5896 V, and the maximum error was \(6.740\times10^{-10}\) V.

## Discussion
Increasing resistance increased the time constant from one second to two seconds. Consequently, the capacitor charged more slowly and reached a lower voltage after five seconds. In both experiments, the numerical solution was extremely close to the exact solution.

## Graph
The numerical and exact charging curves are saved in `plots/Task_18_scipy_ode.png`.

## Conclusion
SciPy's `solve_ivp` provides an effective method for solving ordinary differential equations. The experiment also demonstrates how resistance affects the charging rate of an RC circuit.

