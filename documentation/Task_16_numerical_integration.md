# Task 16: Numerical Integration

## 1. Objective
The objective of this task was to estimate electrical energy consumption from smart-meter power readings using numerical integration.

## 2. Input Data and Mathematical Operations
The program uses power readings in kilowatts recorded every two hours, from hour 0 to hour 12. The time values are stored in a NumPy array, while the power measurements are stored in another array.

Two integration methods are used:
- **Trapezoidal rule:** approximates the area under the power-versus-time curve using trapezoids.
- **Simpson's rule:** approximates the area using parabolic segments.

The area under the power-versus-time curve represents energy consumption, measured in kilowatt-hours (kWh).

## 3. Original Results
Using the original power readings, the trapezoidal rule estimated energy consumption at **15.700 kWh**, while Simpson's rule estimated **15.800 kWh**. The difference between the estimates was 0.100 kWh.

The close estimates indicate that both methods produced similar results for the original data.

## 4. Parameter Modification
The power reading at hour 6 was increased from 1.8 kW to 2.2 kW, while all other readings remained unchanged.

After the modification:
- Trapezoidal estimate: **16.500 kWh**
- Simpson's estimate: **16.867 kWh**
- Difference: **0.367 kWh**

The increased power reading raised both estimates. The difference between the estimates also increased because the two methods approximate the area differently.

## 5. Interpretation
The results demonstrate that numerical integration can estimate accumulated energy from measurements taken at discrete time intervals. The difference between the estimates does not, by itself, establish which method is more accurate; that depends on the actual power curve.

## 6. Real-World Application
Numerical integration can help estimate electricity consumption from smart-meter readings. A household, business or facility could use power measurements collected throughout the day to estimate energy consumption and support energy monitoring.

The accuracy of the estimate depends on the sampling intervals, measurement quality and changes in power between readings.

## 7. Conclusion
This task demonstrated how the trapezoidal and Simpson's rules estimate total energy consumption from power measurements. Changing one reading showed how an increase in measured power affects the calculated energy estimates.