# Task 17: Solving an Ordinary Differential Equation Using Euler's Method

## Objective
To use Euler's method to approximate the temperature of a cooling object and compare the numerical result with the exact solution.

## Method
Newton's law of cooling describes how an object's temperature approaches the surrounding temperature over time. The model used was:

\[
\frac{dT}{dt}=-k(T-T_{\text{ambient}})
\]

The ambient temperature was 25°C, the initial temperature was 90°C, and the cooling constant was 0.12 per minute. Euler's method was used to estimate the temperature over 30 minutes. The result was compared with the exact solution.

## Results

With a step size of 1.0 minute, Euler's method estimated the final temperature as 26.40°C, compared with the exact temperature of 26.78°C. The absolute error was 0.3720°C.

After reducing the step size to 0.5 minutes, the Euler estimate became 26.59°C, while the exact temperature remained 26.78°C. The absolute error decreased to 0.1890°C.

## Discussion
The results show that a smaller step size improves the accuracy of Euler's method for this example. However, the numerical estimate is still an approximation, and its accuracy depends on the chosen step size.

## Graph
The comparison between Euler's method and the exact solution is saved as `plots/Task_17_euler_ode.png`.

## Conclusion
Euler's method can approximate the temperature change of a cooling object. Comparing the numerical approximation with the exact solution helps assess its accuracy and demonstrates the effect of step size.
