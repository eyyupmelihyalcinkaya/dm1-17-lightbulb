import random
import math
from collections import defaultdict
import time

def read_dataset(file_path):
    """Reads a dataset from a text file and returns it as a list of lists."""
    with open(file_path, 'r') as file:
        dataset = [list(map(int, line.strip().split())) for line in file.readlines()]
    return dataset

def may_ozerov_algorithm(dataset, max_iterations=1000):
    """
    May-Ozerov Algorithm to find the pair with the highest correlation.
    
    Inputs:
    - dataset: List of binary vectors (2D list)
    - max_iterations: Maximum number of iterations (default is 1000)

    Returns:
    - The pair of indices with the highest correlation
    """

    n = len(dataset)  # Number of bulbs (samples)
    m = len(dataset[0])  # Number of features (dimensionality of each vector)

    # Step 1: Define some thresholds and parameters
    T0 = int(12 * math.log(n))  # Threshold for pair count (simplified)
    pairs_count = defaultdict(int)  # Dictionary to store pairs and their counts
    max_correlation_pair = None  # To store the pair with the maximum correlation

    # Step 2: Helper function to calculate correlation between two vectors
    def correlation(v1, v2):
        """Calculates the correlation (dot product) between two binary vectors."""
        return sum([x == y for x, y in zip(v1, v2)]) / len(v1)

    # Step 3: Main loop of the algorithm
    for iteration in range(max_iterations):
        # Step 3.1: Initialize buckets (start with all bulbs in one bucket)
        start_time = time.time()  # Start timing the iteration
        buckets = {i: 0 for i in range(n)}  # Mapping of bulb index to bucket

        # Step 3.2: Inner loop for clustering (simulate inner cluster operations)
        for t in range(int(math.log(n))):  # Inner loop: Sample many times
            # Step 3.2.1: Generate the next sample vector (simulated)
            sample = [random.choice([0, 1]) for _ in range(m)]  # Random binary vector of the same length as the dataset

            # Step 3.2.2: Update the buckets based on the sample vector
            for i in range(n):
                buckets[i] = buckets.get(i, 0) + sum([sample[j] == dataset[i][j] for j in range(len(sample))])  # Update bucket value for each bulb

        # Step 3.3: For each bucket, consider all possible pairs of bulbs
        bucket_pairs = defaultdict(int)  # Store pair counts for each bucket
        for i in range(n):
            for j in range(i + 1, n):
                if buckets[i] == buckets[j]:  # Same bucket, consider the pair
                    pair = tuple(sorted([i, j]))  # Ensure uniqueness by sorting
                    bucket_pairs[pair] += 1

        # Step 3.4: Add the pairs to the global count and check if the threshold T0 is reached
        for pair, count in bucket_pairs.items():
            pairs_count[pair] += count
            if pairs_count[pair] >= T0:
                max_correlation_pair = pair
                total_time = time.time() - start_time  # Total time for the iteration
                print(f"Max pair found: {pair} with correlation count: {pairs_count[pair]}")
                print(f"Iteration {iteration + 1} executed in {total_time:.4f} seconds.")
                return max_correlation_pair

        # Measure the total time for the outer loop iterations
        total_time = time.time() - start_time
        print(f"Iteration {iteration + 1} executed in {total_time:.4f} seconds.")

    # If no pair found by the end of iterations, return the most frequent pair
    total_time = time.time() - start_time
    print(f"Algorithm completed in {total_time:.4f} seconds.")

    if max_correlation_pair is None:
        return max(pairs_count, key=pairs_count.get)
    
    return max_correlation_pair


# Example usage
dataset_path = 'dataset.txt'  # Path to your dataset file
dataset = read_dataset(dataset_path)

start_time = time.time()  # Start time for the algorithm
result = may_ozerov_algorithm(dataset)
end_time = time.time()  # End time after the algorithm finishes

print(f"Pair with the maximum correlation: {result}")
total_time = end_time - start_time
print(f"Total time for the May-Ozerov Algorithm: {total_time:.4f} seconds.")
