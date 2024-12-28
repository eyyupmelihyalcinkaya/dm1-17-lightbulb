import numpy as np
from itertools import combinations
from scipy.stats import entropy

def denoise(data, threshold=0.5):
    return (data >= threshold).astype(int)

def mutual_information(data):
    joint = np.apply_along_axis(lambda x: ''.join(map(str, x)), 1, data)
    joint_probs = np.unique(joint, return_counts=True)[1] / data.shape[0]
    marginals = [np.unique(data[:, i], return_counts=True)[1] / data.shape[0]
                 for i in range(data.shape[1])]
    return sum(entropy(p, base=2) for p in marginals) - entropy(joint_probs, base=2)

def k_way_correlation(data, k, threshold=0.5, corr_thresh=0.1):
    true_states = denoise(data, threshold)
    subsets = list(combinations(range(true_states.shape[1]), k))
    results = [(s, mutual_information(true_states[:, s]))
               for s in subsets if mutual_information(true_states[:, s]) >= corr_thresh]
    return results

if __name__ == "__main__":
    np.random.seed(42)
    observations = np.random.rand(100, 5)
    results = k_way_correlation(observations, 3, threshold=0.5, corr_thresh=0.1)
    for subset, score in results:
        print(f"Subset: {subset}, MI: {score:.3f}")
