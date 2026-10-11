# Task 13: Interpolation

## 1. Objective
The objective of this task was to use Python and SciPy to estimate temperature values between known hourly measurements using linear interpolation and cubic spline interpolation.

## 2. Input Data and Mathematical Operations
The program uses hourly measurements from 8:00 AM to 2:00 PM. The temperature readings range from 18.0°C to 25.5°C.

The main operations include:
- Creating NumPy arrays to store the time and temperature measurements.
- Applying `interp1d()` from SciPy to perform linear interpolation.
- Applying `CubicSpline()` to perform cubic spline interpolation.
- Estimating temperatures at specific times and generating a graph of the measurements and interpolation curves.

## 3. Results and Interpretation

The original and modified program produced the following estimates:

| Time | Linear interpolation | Cubic spline |
|---|---:|---:|
| 10:30 AM | 23.25°C | 23.36°C |
| 11:30 AM | 24.50°C | 24.54°C |

The results show that both methods can estimate temperatures between recorded measurements. The cubic spline estimates are slightly higher than the linear estimates at both selected times. The small differences arise because linear interpolation uses straight-line segments, while cubic spline interpolation uses smooth curves.

## 4. Parameter Modification
The target time was changed from 10.5 hours (10:30 AM) to 11.5 hours (11:30 AM).

At 10:30 AM, the linear estimate was 23.25°C and the cubic estimate was 23.36°C. At 11:30 AM, the estimates increased to 24.50°C and 24.54°C, respectively.

This demonstrates that changing the target time changes the estimated temperature according to the measured data and the interpolation method.

## 5. Graph Interpretation
The graph displays the original hourly measurements as scatter points and the linear and cubic interpolation estimates as curves. The curves pass through the measured data points, while the values between those points are estimates. The graph helps compare the smoothness and behaviour of the two methods.

## 6. Real-World Application
Interpolation can be used in weather monitoring systems to estimate temperatures at times when no direct measurement was recorded. For example, a weather station that records temperature hourly could estimate values every ten minutes for more detailed monitoring and reporting.

These estimates depend on the available measurements and the behaviour assumed by the interpolation method. They are not substitutes for actual sensor readings.

## 7. Conclusion
This task demonstrated how NumPy and SciPy can be used to estimate values between known measurements. Linear interpolation provides a straightforward estimate, while cubic spline interpolation provides a smoother curve. Both methods are useful for analysing sampled data and filling gaps between observations.