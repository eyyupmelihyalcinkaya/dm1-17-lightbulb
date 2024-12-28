import math
import numpy as np

def algorithm_Q(X, alpha, gamma):
    n = len(X)  # Get the length of the input list X
    t = 1  # Initialize the time step t
    S = np.zeros((n, n), dtype=int)  # Create an n x n matrix S initialized to zeros
    
    # Initialize Sij
    for i in range(n):
        for j in range(i + 1, n):
            # If elements at position i and j are equal, set S[i][j] and S[j][i] to 1
            if X[i] == X[j]:  
                S[i][j] = 1 
                S[j][i] = 1  
    
    # Calculate the threshold T_prime
    T_prime = 12 * (2 + alpha) * gamma**2 * math.log(n)
    
    while True:
        # Check if any S[i][j] has reached or exceeded the threshold T_prime
        for i in range(n):
            for j in range(i + 1, n):
                if S[i][j] >= T_prime:
                    return (i, j) 
        
        t += 1  
        # Update the matrix S based on the current values of X
        for i in range(n):
            for j in range(i + 1, n):
                if X[i] == X[j]:  
                    S[i][j] += 1  
                    S[j][i] += 1  

# Example usage
X = [1, 2, 1, 3, 2, 1]  # Example input
alpha = 1.5
gamma = 2.0
result = algorithm_Q(X, alpha, gamma)
print("Output pair:", result)
