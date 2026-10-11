# Task 15: Numerical Differentiation

## 1. Objective
The objective of this task was to estimate a vehicle's speed from GPS position measurements using numerical differentiation in Python.

## 2. Input Data and Mathematical Operations
The program uses time measurements in seconds and position measurements in metres. NumPy arrays store the data, while a zero-initialized array stores the estimated speeds.

Three numerical differentiation methods are used:
- **Forward difference:** estimates speed at the first time point.
- **Central difference:** estimates speed at interior time points using measurements before and after each point.
- **Backward difference:** estimates speed at the final time point.

The estimated speed is calculated as the change in position divided by the change in time.

## 3. Original Results
The original estimated speeds were 4.80, 5.10, 5.65, 6.25, 6.95, 7.65 and 8.00 m/s at times from 0 to 6 seconds.

The increasing speed estimates suggest that the vehicle was accelerating during the recorded period.

## 4. Parameter Modification
The final position measurement was changed from 38.0 m to 40.0 m, while all time measurements and other position values remained unchanged.

The estimated speed at 5 seconds increased from 7.65 m/s to 8.65 m/s. The estimated speed at 6 seconds increased from 8.00 m/s to 10.00 m/s. Earlier speed estimates remained unchanged because they did not depend on the modified final measurement.

## 5. Graph Interpretation
The graph displays estimated speed against time. The modified final position produces higher speed estimates near the end of the recorded period. This demonstrates how numerical differentiation responds to changes in measured position data.

## 6. Real-World Application
Numerical differentiation can estimate vehicle speed from GPS measurements when a device records position at regular time intervals. The estimated speed can support vehicle tracking and movement analysis.

The estimates depend on the accuracy and frequency of GPS measurements. Measurement errors may affect the calculated speeds.

## 7. Conclusion
This task demonstrated how forward, central and backward differences can estimate speed from position data. Changing the final position measurement showed how input data affects speed estimates, particularly near the modified measurement.