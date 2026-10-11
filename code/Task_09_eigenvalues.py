
import numpy as np

# Adjacency matrix representing connections between four network nodes

A = np.array([
    [0., 0., 1., 0.],
    [0., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])


# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the dominant eigenvalue
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])

# Calculate normalized eigenvector-based importance scores
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")

for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify the eigenvalue equation
v = np.real(eigenvectors[:, index])
print(
    "Verification error:",
    np.linalg.norm(A @ v - dominant_value * v)
)
