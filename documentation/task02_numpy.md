# Task 2: NumPy Arrays and Numerical Computation

## 1. Mathematical Concept

NumPy arrays store numerical data and allow calculations to be performed efficiently on multiple values. Statistical functions can be used to summarize sensor readings.

## 2. Real-World Problem

Temperature sensors in an IoT monitoring system collect readings from an environment. The system needs to calculate the average, minimum and maximum temperatures to help monitor environmental conditions.

## 3. Input Data

The initial temperature readings are:

`[20, 22, 24, 26, 28]` degrees Celsius.

## 4. Mathematical Operations

- Mean: the sum of all readings divided by the number of readings.
- Minimum: the smallest reading.
- Maximum: the largest reading.

## 5. Implementation

The program is saved as `code/task02_numpy.py`. It uses NumPy functions including `np.mean()`, `np.min()` and `np.max()`.

## 6. Initial Results

- Average temperature: 24°C
- Minimum temperature: 20°C
- Maximum temperature: 28°C

## 7. Parameter Modification and Comparison

**Change made:** The final temperature reading was changed from 28°C to 38°C.

**New results:** Record the average, minimum and maximum values after running the modified program.

**Change made:** The final temperature reading was increased from 28°C to 38°C.

Initial results:

Average temperature: 24°C

Minimum temperature: 20°C

Maximum temperature: 28°C

Modified results:

Average temperature: 26°C

Minimum temperature: 20°C

Maximum temperature: 38°C

Interpretation: Increasing the final reading by 10°C increased the average temperature by 2°C, from 24°C to 26°C. The maximum temperature increased from 28°C to 38°C, while the minimum remained at 20°C because the smallest reading was unchanged.

## 8. Related Real-World Application

The same approach can be applied to an IoT environmental monitoring system that summarizes temperature measurements and identifies unusually high readings.

## 9. Conclusion

Summarize what the calculations demonstrate and how the results could help monitor environmental conditions.