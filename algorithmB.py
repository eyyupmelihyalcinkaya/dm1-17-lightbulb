import random
import math
from collections import defaultdict
import time

def read_dataset(file_path):
    with open(file_path, 'r') as file:
        dataset = [list(map(int, line.strip().split())) for line in file.readlines()]
    return dataset

def algorithm_b(dataset, p1, gamma, alpha, q2, max_iterations=1000):
    n = len(dataset)  # Number of bulbs (samples)
    # Calculate the threshold T0 for pair count
    start_time = time.time()
    T0 = int(12 * (2 + alpha) * gamma**2 * math.log(n))  # Threshold for pair count
    time_to_compute_T0 = time.time() - start_time
    print(f"Time to compute T0: {time_to_compute_T0:.4f} seconds")
    pairs_count = defaultdict(int)  # Dictionary to store pairs and their counts
    max_correlation_pair = None
    # Helper function to calculate correlation between two vectors
    def correlation(v1, v2):
        return sum([x == y for x, y in zip(v1, v2)]) / len(v1)
    # Main loop of the algorithm
    for iteration in range(max_iterations):
        # Initialize buckets (start with all bulbs in one bucket)
        start_time = time.time()
        buckets = {i: 0 for i in range(n)}  # Mapping of bulb index to bucket
        # Inner loop for sampling
        for t in range(int(math.log(n) / math.log(1 / q2))):  # Inner loop: Sample many times
            # Generate the next sample vector
            sample = [random.choice([0, 1]) for _ in range(len(dataset[0]))]  # Random binary vector of the same length as the dataset
            # Update the buckets based on the sample vector
            for i in range(n):
                buckets[i] = buckets.get(i, 0) + sum([sample[j] == dataset[i][j] for j in range(len(sample))]) # Update bucket value for each bulb
        # For each bucket, consider all possible pairs of bulbs
        bucket_pairs = defaultdict(int)  # Store pair counts for each bucket
        for i in range(n):
            for j in range(i + 1, n):
                if buckets[i] == buckets[j]:  # Same bucket, consider the pair
                    pair = tuple(sorted([i, j]))  # Ensure uniqueness by sorting
                    bucket_pairs[pair] += 1
        
        # Add the pairs to the global count and check if the threshold T0 is reached
        for pair, count in bucket_pairs.items():
            pairs_count[pair] += count
            if pairs_count[pair] >= T0:
                max_correlation_pair = pair
                total_time = time.time() - start_time
                print(f"Max pair found: {pair} with correlation count: {pairs_count[pair]}")
                print(f"Iteration {iteration + 1} executed in {total_time:.4f} seconds.")
                return max_correlation_pair
        
        # Measure the total time for the outer loop iterations
        total_time = time.time() - start_time
        print(f"Iteration {iteration + 1} executed in {total_time:.4f} seconds.")
    
    # If no pair found by the end of iterations, return the most frequent pair
    total_time = time.time() - start_time
    print(f"Algorithm B completed in {total_time:.4f} seconds.")
    if max_correlation_pair is None:
        return max(pairs_count, key=pairs_count.get)
    return max_correlation_pair

# Example usage
dataset_path = 'dataset.txt'
dataset = read_dataset(dataset_path)

p1 = 1  # Correlation of the most similar pair
gamma = 2  # Accuracy parameter
alpha = 1  # Certainty parameter
q2 = 0.5  # Upper bound on second largest correlation

start_time = time.time()
result = algorithm_b(dataset, p1, gamma, alpha, q2)
end_time = time.time()

print(f"Pair with the maximum correlation: {result}")
total_time = end_time - start_time
print(f"Algorithm B completed in {total_time:.4f} seconds.")
