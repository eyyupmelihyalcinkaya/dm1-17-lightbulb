DM1-17 Light Bulb Problem


Abstract

The light bulb problem and the closed-pair problem represent foundational challenges in data analysis and theoretical computer science, involving the identification of correlated or closest vector pairs within large datasets. The first paper proposes a faster randomized algorithm for finding the closest pairs in the Hamming metric, outperforming existing methods when the vector dimensions are small relative to the size of the data set. Its modular analysis simplifies previous approaches and extends applicability to nonuniform distributions, demonstrating practical feasibility through proof-of-concept implementation. The second paper introduces an efficient algorithm that leverages the polynomial method for the Light Bulb Problem, matching state-of-the-art runtimes while offering simpler analysis and deterministic solutions. Both works advance algorithmic efficiency in high-dimensional spaces with applications in cryptography, machine learning, and genome studies.

The DM1-17 Light Bulb Problem project explores efficient algorithms for identifying correlated pairs within large datasets, 
particularly binary vectors. These algorithms address foundational challenges in computational theory and have applications in fields such as cryptography, 
bioinformatics, and machine learning.

Features
Algorithm Q: A quadratic approach that finds the most correlated pair through direct sampling.
Algorithm B: A subquadratic algorithm leveraging bucket-based grouping for efficiency.
Generalized k-Way Correlation Algorithm: Analyzes higher-order correlations for groups of variables.
Polynomial Analysis: Utilizes recursive bucketing and random projections for scalable analysis.
May-Ozerov Algorithm: Adapts locality-sensitive hashing for efficient correlation detection.

Requirements
Python 3.7 or higher

Libraries: numpy, math, collections

Installation
Clone the repository:
git clone https://github.com/eyyupmelihyalcinkaya/dm1-17-lightbulb.git

Install dependencies:
pip install -r requirements.txt

Usage

Run the desired algorithm script, for example:
python algorithmQ.py
