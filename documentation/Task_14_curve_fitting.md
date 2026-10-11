# Task 14: Curve Fitting and Approximation

## 1. Objective
The objective of this task was to use Python and SciPy to fit a mathematical curve to measured server response-time data and predict response time at higher user loads.

## 2. Input Data and Mathematical Operations
The program uses the number of concurrent users as the independent variable and measured server response time in milliseconds as the dependent variable.

The number of users is `[50, 100, 150, 200, 250, 300, 350]`, while the corresponding response times are `[82, 95, 115, 145, 185, 238, 305]` milliseconds.

The program uses `curve_fit()` from SciPy to estimate the parameters of a quadratic model:

**y = ax² + bx + c**

It then calculates predicted response times and the root mean square error (RMSE), which measures the difference between measured and predicted values.

## 3. Original Results
The fitted model was approximately:

**y = 0.002167x² − 0.1345x + 85.00**

The RMSE was **1.55 ms**, and the predicted response time at 400 concurrent users was **377.86 ms**.

The low RMSE indicates that the fitted curve closely represents the supplied measurements.

## 4. Parameter Modification
The prediction target was changed from 400 to 450 concurrent users. The predicted response time increased from 377.86 ms to **463.21 ms**.

The RMSE remained 1.55 ms because the model and measured data were unchanged. Only the input used for the prediction was modified.

## 5. Graph Interpretation
The graph displays the measured response times as scatter points and the fitted quadratic curve as a continuous line. The curve represents the relationship estimated from the observations.

The model predicts that response time increases as the number of concurrent users grows. Predictions beyond the observed range are extrapolations and may be less reliable than estimates within that range.

## 6. Real-World Application
Curve fitting can help system administrators understand how server response time changes as more users access an application. Such a model can support capacity planning and performance analysis.

For example, a developer could measure response times at different loads and fit a curve to estimate the response time at a higher load. The prediction should be validated through actual load testing before being used for important capacity decisions.

## 7. Conclusion
This task demonstrated how SciPy can fit a quadratic model to measured data and use it to estimate server response time. The RMSE provided a measure of model fit, while changing the prediction target showed how the model can estimate performance at different user loads.