# Chapter 5: Optimizing Code with and Without Big O

### 1. Selection Sort

- Selection Sort sorts an array by repeatedly finding the smallest value in the unsorted portion and swapping it into its correct position.
- Each pass-through:
  1. Find the smallest value in the remaining array.
  2. Store its index.
  3. Swap it with the first value in the unsorted portion.
  4. Repeat until the array is sorted.

Example:

```
[4, 2, 7, 1, 3]
[1, 2, 7, 4, 3]
[1, 2, 7, 4, 3]
[1, 2, 3, 4, 7]
```

### 2. Selection Sort vs. Bubble Sort

Both algorithms have O(N²) time complexity, but Selection Sort generally performs fewer steps.

| Algorithm      | Comparisons | Swaps       |
| -------------- | ----------- | ----------- |
| Bubble Sort    | O(N²)       | Up to O(N²) |
| Selection Sort | O(N²)       | Up to O(N)  |

- Selection Sort performs at most one swap per pass-through.
- Bubble Sort may perform a swap after every comparison.
- Selection Sort can therefore be faster despite both having the same Big O classification.

### 3. Big O Ignores Constants

Big O ignores constant factors because it focuses on how an algorithm's running time grows as input size increases.

Examples:

| Expression | Big O |
| ---------- | ----- |
| N / 2      | O(N)  |
| 2N         | O(N)  |
| 100N       | O(N)  |
| N² / 2     | O(N²) |
| N² + 10    | O(N²) |

Important: Constants affect actual execution speed but do not change the Big O classification.

### 4. Big O Categories

Big O groups algorithms into general efficiency categories based on their growth rates.

- O(1): Constant time.
- O(log N): Logarithmic time.
- O(N): Linear time.
- O(N²): Quadratic time.

The key difference is their growth rate as input size increases.

For example:

- O(100N) and O(N) belong to the same category.
- O(N) and O(N²) belong to different categories.
- Eventually, O(N²) becomes slower than any constant multiple of O(N) as N grows sufficiently large.

### 5. Comparing Algorithms Within the Same Big O Category

Two algorithms can have the same Big O complexity but different actual running times.

Example: Printing even numbers

Version 1:

```
number = 2while number <= upperLimit:    if number % 2 == 0:        print(number)    number += 1
```

Version 2:

```
number = 2while number <= upperLimit:    print(number)    number += 2
```

| Algorithm | Approximate iterations | Big O |
| --------- | ---------------------- | ----- |
| Version 1 | N                      | O(N)  |
| Version 2 | N/2                    | O(N)  |

- Version 1 checks every number to determine whether it is even.
- Version 2 skips odd numbers by incrementing by 2.
- Version 2 is approximately twice as fast, even though both are O(N).

Lesson: Big O alone cannot determine which of two algorithms in the same category is faster. Further analysis is necessary.

### 6. Significant Steps

When calculating time complexity, count all significant operations, including:

- Comparisons.
- Assignments and increments.
- Printing/output operations.
- Other operations performed during execution.

Example: An algorithm performs:

- N comparisons.
- N increments.
- N/2 print operations.

Total:

\\[ N + N + \frac{N}{2} = 2.5N \\]

Therefore:

\\[ O(2.5N) = O(N) \\]

All operations matter when counting steps, but constant factors are dropped when expressing the final Big O complexity.

### Key Takeaways

1. Selection Sort: Repeatedly finds the minimum value and swaps it into its correct position. Its time complexity is O(N²).
2. Big O ignores constants: O(2N), O(100N), and O(N) all belong to the same category.
3. Same Big O doesn't mean same speed: Two O(N²) algorithms can have significantly different execution times.
4. Different categories matter: O(N) grows more slowly than O(N²) as input size increases.
5. Count all significant steps: Comparisons, assignments, increments, and other operations contribute to an algorithm's total steps.
6. Optimize beyond Big O: When algorithms share the same Big O classification, examine their actual operations and number of steps to identify the faster implementation.

Central lesson: Big O helps compare algorithms by their growth rates, but choosing the fastest algorithm sometimes requires looking beyond Big O and counting the actual operations performed.
