# Task 3: Mathematical Functions and Vectorization

## 1. Mathematical Concept

Vectorization is the process of applying a mathematical operation to multiple values at the same time. NumPy allows calculations to be performed on an entire array without explicitly writing a Python loop for every element.

## 2. Real-World Problem

A network-monitoring system processes one million network latency measurements. Each measurement must be converted from milliseconds to seconds, and the converted value must be squared for an error calculation.

## 3. Input Data

The program generates one million simulated latency readings between 5 and 250 milliseconds using NumPy's random-number generator with seed 42.

## 4. Mathematical Operations

The conversion from milliseconds to seconds is:

seconds = latency_ms / 1000

The squared latency is calculated as:

squared = seconds²

The program compares the execution time of a Python loop with the vectorized NumPy implementation using `timeit`.

## 5. Implementation

The program is saved as `code/task_03_vectorization.py`.

The loop implementation processes each measurement individually. The vectorized implementation divides the entire array by 1000 and squares all converted values in array operations.

## 6. Results and Interpretation

The first five squared latency values were approximately:

`[0.03787665, 0.01266192, 0.04637842, 0.03092504, 0.00078812]`

The Python loop took 0.4036 seconds, while the vectorized implementation took an average of 0.0043 seconds. The measured speed-up was approximately 93.4 times.

These results show that vectorization can greatly reduce computation time when processing large numerical datasets.

## 7. Parameter Modification and Comparison

The program's input parameter can be changed by modifying the number of generated latency measurements. This allows the effect of dataset size on execution time to be investigated.

After changing the dataset size, rerun the program and record the new loop time, vectorized time and speed-up here.

## 8. Related Real-World Application

The same method can be used in network-monitoring systems to process large volumes of latency data, convert units and calculate error-related quantities efficiently.

## 9. Conclusion

The experiment demonstrates that NumPy vectorization can perform numerical calculations more efficiently than an explicit Python loop for a large dataset. The measured performance difference supports the use of vectorized operations in scientific computing.