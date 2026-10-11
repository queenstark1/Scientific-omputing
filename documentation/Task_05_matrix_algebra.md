# Task 5: Matrix Algebra and Matrix Operations

## 1. Objective
To use NumPy matrices to rotate and scale two-dimensional points and examine the determinant of the resulting transformation matrix.

## 2. Input Values
- Four square corners: (0,0), (1,0), (1,1), and (0,1).
- Rotation angle: 45 degrees initially.
- Horizontal scaling factor: 2.0.
- Vertical scaling factor: 1.5.

## 3. Mathematical Operations
The program converts the angle from degrees to radians, constructs rotation and scaling matrices, combines them using matrix multiplication, and transforms the coordinates. It also calculates the determinant.

## 4. Initial Results
At 45 degrees, the point (1,0) becomes approximately (1.414, 1.414), while the point (1,1) becomes approximately (0.354, 2.475). The determinant is approximately 3.

## 5. Parameter Change
The rotation angle was changed from 45 degrees to 90 degrees, while both scaling factors remained unchanged.

At 90 degrees, the point (1,0) becomes approximately (0, 2), and the point (1,1) becomes approximately (-1.5, 2). The determinant remains approximately 3.

## 6. Interpretation
Changing the angle changes the orientation and coordinates of the square. The determinant remains approximately 3 because the scaling factors are unchanged. Its absolute value indicates that the transformed shape has three times the original area. Very small values close to zero in the output result from floating-point approximations.

## 7. Related Real-World Application
The same technique can be used in computer graphics to rotate and resize objects. For example, a graphics application can transform the coordinates of a two-dimensional object before displaying it in a different orientation or size.

## 8. Conclusion
NumPy matrix operations provide an efficient way to apply geometric transformations to multiple points. The experiment demonstrates how changing a parameter affects the output and how the determinant helps describe the transformation.