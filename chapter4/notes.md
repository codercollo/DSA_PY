# Chapter 4: Speeding Up Your Code with Big O

## 1. Why Big O Matters

- Big O measures how an algorithm's efficiency grows as input size (N) increases.
- Helps compare algorithms and identify inefficient solutions.
- Optimization involves finding ways to reduce time complexity.
- Prefer faster Big O categories where possible.

| Complexity | Name        | Performance |
| ---------- | ----------- | ----------- |
| O(1)       | Constant    | Excellent   |
| O(log N)   | Logarithmic | Very fast   |
| O(N)       | Linear      | Good        |
| O(N²)      | Quadratic   | Slow        |

## 2. Bubble Sort

Definition: A simple sorting algorithm that arranges array elements in ascending order by repeatedly comparing adjacent elements and swapping them when they are out of order.

How it works:

1. Compare two adjacent elements.
2. If the left element is greater, swap them.
3. Move to the next pair.
4. Repeat until the end of the array (one pass).
5. Repeat passes until a complete pass occurs without any swaps.

Example:

```
[4, 2, 7, 1, 3]# After sorting:[1, 2, 3, 4, 7]
```

Key concept: The largest unsorted value bubbles to its correct position during each pass.

### Bubble Sort implementation

```
def bubble_sort(array):    unsorted_until_index = len(array) - 1    sorted = False    while not sorted:        sorted = True        for i in range(unsorted_until_index):            if array[i] > array[i + 1]:                array[i], array[i + 1] = array[i + 1], array[i]                sorted = False        unsorted_until_index -= 1    return array
```

Important variables:

- `unsorted_until_index`: Tracks the rightmost unsorted position.
- `sorted`: Tracks whether any swaps occurred during a pass.
- If no swaps occur, the array is sorted and the algorithm terminates.

## 3. Bubble Sort Time Complexity

Bubble Sort performs two main operations:

- Comparisons: Checking whether adjacent elements are in the correct order.
- Swaps: Exchanging elements that are out of order.

For N elements, comparisons are:

\\[ (N-1)+(N-2)+\cdots+1 \\]

This produces quadratic growth, approximately \\(N^2/2\\).

| Elements (N) | Comparisons | Approx. total steps (worst case) |
| ------------ | ----------- | -------------------------------- |
| 5            | 10          | 20                               |
| 10           | 45          | 90                               |
| 20           | 190         | 380                              |
| 40           | 780         | 1,560                            |
| 80           | 3,160       | 6,320                            |

Time Complexity: O(N²) — Quadratic Time

- Nested passes cause the number of operations to grow quadratically.
- Doubling the input size approximately quadruples the work.
- Considered inefficient for large datasets.

## 4. Recognizing Quadratic Problems (O(N²))

A common source of quadratic algorithms is nested loops.

Example: Finding duplicate values using nested loops.

```
function hasDuplicateValue(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if (i !== j && array[i] === array[j]) {
                return true;
            }
        }
    }
    return false;
}
```

Logic:

- Outer loop selects an element.
- Inner loop compares it against every other element.
- If a matching value is found at a different index, return `true`.
- If no matches exist, return `false`.

Why O(N²)?

For every N elements, the inner loop runs N times:

\\[ N \times N = N^2 \\]

Example: 5 elements = 25 comparisons (worst case).

Lesson: Whenever you encounter nested loops, investigate whether the algorithm has O(N²) complexity.

## 5. Optimizing Quadratic Algorithms: O(N²) → O(N)

The same duplicate-detection problem can be solved using a single loop and an auxiliary array.

### Linear solution

```
function hasDuplicateValue(array) {
    let existingNumbers = [];

    for (let i = 0; i < array.length; i++) {
        if (existingNumbers[array[i]] === 1) {
            return true;
        } else {
            existingNumbers[array[i]] = 1;
        }
    }

    return false;
}
```

Logic:

1. Create an empty `existingNumbers` array to remember previously encountered numbers.
2. Iterate through the input array once.
3. Check whether the current number's index in `existingNumbers` already contains `1`.
4. If it does, the number has appeared before → return `true`.
5. Otherwise, store `1` at that index to mark the number as seen.
6. If the loop finishes without finding a duplicate → return `false`.

Example:

Input:

```
[3, 5, 8, 5]
```

| Number | Already seen? | Action       |
| ------ | ------------- | ------------ |
| 3      | No            | Mark index 3 |
| 5      | No            | Mark index 5 |
| 8      | No            | Mark index 8 |
| 5      | Yes           | Return true  |

### Why O(N)?

- Only one loop is used.
- Each element is checked once.
- N elements require N iterations in the worst case.

\\[ O(N) \\]

Trade-off: The optimized solution uses additional memory to store previously encountered numbers. It saves execution time at the cost of extra space.

Note: The array-index technique assumes non-negative integer values within a reasonably manageable range.

## 6. Comparing Both Approaches

| Feature         | Nested loops         | Auxiliary array                 |
| --------------- | -------------------- | ------------------------------- |
| Time complexity | O(N²)                | O(N)                            |
| Loops           | Two nested loops     | One loop                        |
| Memory          | O(1) auxiliary       | O(K) auxiliary                  |
| Speed           | Slower               | Faster                          |
| Strategy        | Repeated comparisons | Remember previously seen values |

Here, K represents the range of possible number values used as indexes.

## 7. Key Lessons from Chapter 4

1. Big O helps identify inefficiency: Use it to evaluate how algorithms scale.
2. Bubble Sort: Adjacent comparisons and swaps; O(N²).
3. Nested loops: Often indicate quadratic time complexity.
4. Avoid repeated work: Store useful information to avoid unnecessary comparisons.
5. Auxiliary data structures: Arrays can help optimize algorithms by remembering previously processed values.
6. Optimization trade-off: Faster execution may require additional memory.

## Quick Revision Cheat Sheet

| Concept         | Remember                                         |
| --------------- | ------------------------------------------------ |
| O(N)            | One pass through N elements                      |
| O(N²)           | Nested loops; N × N work                         |
| Bubble Sort     | Largest unsorted value bubbles to the right      |
| Comparison      | Checks the relationship between values           |
| Swap            | Exchanges two elements                           |
| Auxiliary array | Extra storage used to optimize processing        |
| Optimization    | Reduce repeated work and improve time complexity |

The biggest takeaway from Chapter 4

Don't just ask whether your algorithm works. Ask whether it does unnecessary work.

An O(N²) solution may work correctly, but by remembering previously processed information, you may be able to redesign it as O(N).

Think about both time and memory when optimizing algorithms.
