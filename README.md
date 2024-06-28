# Data-Structures-and-Algorithms-for-Biology
This repository contains all material related to the course Data Structures and Algorithms for Biology (BT3051) in the Fall 2023 semester.

## Course Objectives
* Equip you with the fundamentals of algorithms (problem-solving methods) and data structures (information storage methods).
* Explore algorithms and data structures specifically relevant to biological applications.
* Enhance your programming skills through good coding practices.

## Course Outcomes
By the end of the course, I was able to:
* Grasp the core concepts of fundamental algorithms and data structures, including their time and space complexity analysis using Big O notation (e.g., O(n log n) for efficient sorting algorithms).
* Apply general computational techniques like dynamic programming (solving complex problems by breaking them down into memoized subproblems) and randomization (using random numbers to solve problems efficiently) to solve biological problems.
* Leverage standard libraries in Python (like NumPy for numerical computing and Biopython for biological sequence analysis) to tackle biological challenges programmatically.
* Develop my own algorithms and data structures tailored to address specific biological problems, considering factors like data size and access patterns.
* Write, test, and maintain clean, readable, and well-documented Python code that adheres to professional standards using version control systems (like Git) for code management.

## Course Content
The course delves into various topics, providing a well-rounded foundation in computational biology:
- `Introduction + Python/Programming Basics`: This helped me establish a strong foundation in Python, a popular language for biological computing. This includes learning essential programming concepts (variables, data types, control flow, functions) and syntax.
- `Introduction to Algorithms and Data Structures`: This module introduces core algorithmic concepts like searching (linear search, binary search for sorted data), sorting (bubble sort, insertion sort, merge sort with divide-and-conquer, quick sort with pivoting), and efficiency analysis using Big O notation to understand how algorithm performance scales with input size. We also explored fundamental data structures such as arrays (random access, fixed size), linked lists (dynamic size, efficient insertions/deletions), stacks (LIFO - Last In First Out - for implementing undo/redo functionality), queues (FIFO - First In First Out - for processing data in arrival order), and trees (hierarchical structures for efficient searching and sorting).
- `Sorting Algorithms & Dynamic Programming`: We delved into advanced sorting algorithms like merge sort (efficient for large datasets) and quick sort (efficient on average for most inputs) and explored their time and space complexity. Dynamic programming, a powerful technique for solving complex problems by breaking them down into memoized subproblems (storing solutions to subproblems to avoid redundant calculations), was be explored in the context of string alignment.
- `String Algorithms`: Biological data often involves sequences like DNA or protein structures. This section equips you with algorithms for string manipulation (slicing, concatenation), and pattern matching (finding specific subsequences within a larger string using Knuth-Morris-Pratt algorithm).
- `Graph Algorithms`: Biological systems can be modeled as networks (graphs) where entities (nodes, e.g., genes) are connected by interactions (edges, e.g., protein-protein interactions). We'll explore algorithms for graph traversal (depth-first search for exploring connected components, breadth-first search for finding shortest paths), and shortest path calculations (Dijkstra's algorithm).
- `Random Numbers & Sampling`: Randomness plays a crucial role in biological simulations (e.g., modeling mutations) and modeling (e.g., Monte Carlo simulations). This module covers techniques for generating random numbers using pseudo-random number generators (PRNGs) and employing them in sampling strategies for data analysis (e.g., random sampling, stratified sampling for ensuring representativeness).
- `Direct Search Algorithms & Evolutionary Algorithms`: We explored optimization techniques like direct search algorithms (iteratively searching for solutions that improve a specific objective function, e.g., hill climbing), Simulated Annealing and looked at potential applications to introduce evolutionary algorithms inspired by natural selection for solving problems in biological domains.
