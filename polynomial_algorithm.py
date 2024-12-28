import numpy as np
from itertools import combinations

def generate_light_bulb_data(n, d, rho):
    """
    Generate data for the Light Bulb Problem with a planted correlated pair.

    Args:
        n (int): Number of vectors.
        d (int): Dimensions of each vector.
        rho (float): Correlation coefficient for the planted pair.

    Returns:
        tuple: Array of vectors, indices of the planted pair.
    """
    vectors = np.random.choice([-1, 1], size=(n, d))
    i, j = np.random.choice(n, size=2, replace=False)

    overlap = int(rho * d)
    indices = np.random.choice(d, size=overlap, replace=False)
    vectors[j, indices] = vectors[i, indices]  # Plant the correlation

    return vectors, (i, j)

def cosine_similarity(v1, v2):
    """
    Compute cosine similarity between two vectors.
    """
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def recursive_bucketing(vectors, indices, depth, max_depth, random_seed):
    """
    Perform recursive bucketing to isolate correlated pairs.

    Args:
        vectors (np.ndarray): Dataset of vectors.
        indices (list): Current indices being processed.
        depth (int): Current recursion depth.
        max_depth (int): Maximum recursion depth.
        random_seed (int): Seed for random projection.

    Returns:
        tuple: Detected pair of indices.
    """
    if len(indices) < 2:
        return None  # No pair can be formed
    if depth > max_depth:
        # Brute force at maximum depth
        return max(
            combinations(indices, 2),
            key=lambda pair: cosine_similarity(vectors[pair[0]], vectors[pair[1]]),
            default=None
        )

    # Random projection for bucketing
    np.random.seed(random_seed + depth)
    projection = np.random.randn(vectors.shape[1])
    buckets = {}
    for i in indices:
        key = np.dot(vectors[i], projection)
        buckets.setdefault(key, []).append(i)

    # Process each bucket recursively
    for bucket_indices in buckets.values():
        if len(bucket_indices) > 1:
            result = recursive_bucketing(vectors, bucket_indices, depth + 1, max_depth, random_seed)
            if result:
                return result

    # Fallback: Brute force on all remaining indices
    return max(
        combinations(indices, 2),
        key=lambda pair: cosine_similarity(vectors[pair[0]], vectors[pair[1]]),
        default=None
    )

def solve_light_bulb(vectors, max_depth=5, random_seed=42):
    """
    Solve the Light Bulb Problem using recursive bucketing with random projections.

    Args:
        vectors (np.ndarray): Dataset of vectors.
        max_depth (int): Maximum recursion depth.
        random_seed (int): Seed for random projection.

    Returns:
        tuple: Detected pair of indices.
    """
    indices = list(range(len(vectors)))
    return recursive_bucketing(vectors, indices, 0, max_depth, random_seed)

# Example Usage
if __name__ == "__main__":
    n, d = 10000, 1000  # 100 vectors in 300 dimensions
    rho = 0.8  # Strong correlation

    # Generate dataset
    vectors, planted_pair = generate_light_bulb_data(n, d, rho)
    print("Planted Pair:", planted_pair)

    # Solve the Light Bulb Problem
    detected_pair = solve_light_bulb(vectors)
    if detected_pair is None:
        print("No pair detected!")
    else:
        # Normalize the order of pairs for comparison
        planted_pair = tuple(sorted(planted_pair))
        detected_pair = tuple(sorted(detected_pair))

        print("Detected Pair:", detected_pair)

        # Validate the detected pair
        planted_corr = cosine_similarity(vectors[planted_pair[0]], vectors[planted_pair[1]])
        detected_corr = cosine_similarity(vectors[detected_pair[0]], vectors[detected_pair[1]])
        print("Validation Result:")
        print(f"Planted Correlation: {planted_corr:.2f}")
        print(f"Detected Correlation: {detected_corr:.2f}")
        print(f"Match: {detected_pair == planted_pair}")
