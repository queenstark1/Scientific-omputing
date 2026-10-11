# Task 9: Eigenvalues and Eigenvectors

## 1. Problem Description

This task uses NumPy to calculate the eigenvalues and eigenvectors of an adjacency matrix representing a network of four nodes: A, B, C and D. The dominant eigenvector is used to estimate the relative importance of each node.

## 2. Input Values

The input is a 4 × 4 adjacency matrix. A value of 1 represents a direct connection between two nodes, while 0 represents the absence of a direct connection.

## 3. Mathematical Operations

The program uses `np.linalg.eig(A)` to calculate the eigenvalues and eigenvectors. It selects the eigenvector associated with the dominant eigenvalue, takes the absolute values of its components and normalizes them so that the importance scores sum to approximately 1.

The verification error is calculated using the eigenvalue equation \(Av=\lambda v\).

## 4. Original Results

The dominant eigenvalue was approximately 2.5616. The original importance scores were:

- Node A: 0.2192
- Node B: 0.2808
- Node C: 0.2808
- Node D: 0.2192

Nodes B and C had the highest importance scores in the original network.

## 5. Parameter Change and Interpretation

The direct connection between nodes A and B was removed by setting the corresponding entries in the adjacency matrix to zero.

The modified dominant eigenvalue was approximately 2.1701. The new importance scores were:

- Node A: 0.1454
- Node B: 0.2696
- Node C: 0.3154
- Node D: 0.2696

Node A's score decreased, while node C became the most important node under the eigenvector-based measure. The scores changed because the network's connection structure changed.

## 6. Real-World Application

Eigenvector-based importance can be used to analyse communication networks, social networks and connected systems. A node may be considered more important when its connections link it to other influential nodes.

## 7. Conclusion

The experiment demonstrated that eigenvalues and eigenvectors can be used to estimate node importance in a network. Removing one connection changed both the dominant eigenvalue and the distribution of importance scores. The verification errors were close to zero, confirming the numerical consistency of the calculated eigenpairs.