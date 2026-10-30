# Chapter 3: O Yes! Big O Notation

Data Structures & Algorithms — Summary Notes

## 1. What is Big O Notation?

- Big O Notation is a mathematical way of describing an algorithm's efficiency based on how its number of steps grows as the input size increases.
- It provides a consistent way to compare algorithms regardless of the actual number of steps for a particular input.
- Instead of saying an algorithm takes 22 or 400 steps, we describe its growth relative to N.

N = Number of input elements (or input size).

Key question:

> If there are N data elements, how many steps will the algorithm take?

Example:

- Linear search through 22 elements → up to 22 steps.
- Linear search through 400 elements → up to 400 steps.
- Therefore, linear search has O(N) time complexity.

## 2. The Three Main Time Complexities

### A. O(1) — Constant Time

- Number of steps remains constant regardless of input size.
- Increasing the data does not increase the number of operations.
- Also called constant time.

Example: Reading an array element by index.

```
function getFirst(array) {
    return array[0];
}
```

Whether the array contains 10 or 1 million elements, accessing an element by index takes a constant number of operations.

Graph behavior: Horizontal line — performance remains constant as N increases.

### B. O(N) — Linear Time

- Number of steps increases proportionally with input size.
- Every additional element adds approximately one additional step.
- Also called linear time.

Example: Linear search or iterating through an array.

```
function printItems(array) {
    for (const item of array) {
        console.log(item);
    }
}
```

| Input size (N) | Steps |
| -------------- | ----- |
| 10             | 10    |
| 100            | 100   |
| 1,000          | 1,000 |

Graph behavior: Diagonal straight line — steps grow proportionally with N.

### C. O(log N) — Logarithmic Time

- Number of steps increases by one whenever the input size doubles.
- Each operation reduces the remaining search space, typically by half.
- Much more efficient than O(N) for large inputs.
- Also called logarithmic time.

Example: Binary search on a sorted array.

```
function binarySearch(array, target) {
    // Repeatedly eliminates half the search space.
}
```

| Input size (N) | O(log N) steps |
| -------------- | -------------- |
| 8              | 3              |
| 16             | 4              |
| 32             | 5              |
| 64             | 6              |
| 128            | 7              |
| 256            | 8              |
| 512            | 9              |
| 1,024          | 10             |

Graph behavior: Slowly increasing curve — input can grow significantly with only a small increase in steps.

## 3. The Soul of Big O

Big O is not primarily concerned with the exact number of steps an algorithm takes.

It focuses on how an algorithm's performance changes as the input size increases.

For example:

- O(1) and O(3) are both classified as O(1).
- Both represent constant-time algorithms.
- We ignore constant differences because they do not change the algorithm's growth pattern.

Important: An algorithm taking 100 constant steps (O(1)) can eventually outperform an O(N) algorithm as the input grows.

Even if O(N) initially takes fewer steps, it eventually takes more steps than the constant-time algorithm.

## 4. Best-Case vs Worst-Case Complexity

The same algorithm can have different time complexities depending on the scenario.

Example: Linear search.

```
function linearSearch(array, target) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === target) {
            return i;
        }
    }
    return -1;
}
```

- Best case — O(1): Target is found in the first element.
- Worst case — O(N): Target is in the last element or doesn't exist.

Important: Big O generally describes the worst-case scenario unless otherwise specified.

Why? It helps us understand the maximum amount of work an algorithm might require.

## 5. Understanding Logarithms

A logarithm is the inverse of an exponent.

For example:

\\[ 2^3 = 8 \\]

Therefore:

\\[ \log_2 8 = 3 \\]

Meaning: How many times must we multiply 2 by itself to get 8?

Another way to understand logarithms:

How many times can we divide a number by 2 until we reach 1?

Example:

\\[ 64 \div 2 \div 2 \div 2 \div 2 \div 2 \div 2 = 1 \\]

Therefore:

\\[ \log_2 64 = 6 \\]

### O(log N) in algorithms

- O(log N) is shorthand for O(log₂ N).
- It describes algorithms that repeatedly halve their input/search space.
- Binary search is the classic example.

Remember: Doubling the input adds just one extra step in logarithmic time.

## 6. Comparing the Three Complexities

Efficiency ranking (most efficient to least efficient)

1\. O(1)

Constant

Unaffected by input growth.

2\. O(log N)

Logarithmic

Grows slowly as input increases.

3\. O(N)

Linear

Grows proportionally with input size.

## 7. Practical Examples

Example 1: Printing every item in a list

```
for thing in things:    print(thing)
```

- Every element is processed once.
- N elements = N iterations.
- Complexity: O(N).

Example 2: Checking whether a number is prime

```
def is_prime(number):    for i in range(2, number):        if number % i == 0:            return False    return True
```

- The loop checks integers from 2 up to the given number.
- Larger numbers generally require more iterations.
- Complexity: O(N) (worst case).

Important: N does not always represent an array's length. It represents the size of the input being processed. Here, N is the input number.

## 8. Quick Revision Cheat Sheet

| Big O    | Name        | Growth behavior            | Typical example    |
| -------- | ----------- | -------------------------- | ------------------ |
| O(1)     | Constant    | No growth                  | Array index access |
| O(log N) | Logarithmic | +1 step when input doubles | Binary search      |
| O(N)     | Linear      | Doubles when input doubles | Array traversal    |

## 9. Key Takeaways

1. Big O describes how an algorithm's steps grow relative to input size.
2. Always ask: If there are N inputs, how many steps will the algorithm take?
3. O(1) means constant operations regardless of input size.
4. O(N) means operations grow proportionally with input size.
5. O(log N) means the algorithm typically halves the search space each step.
6. Big O focuses on growth patterns, not exact step counts.
7. Big O generally refers to worst-case complexity unless specified otherwise.
8. N represents the input size, not necessarily the number of array elements.

Chapter 3 completed

The most important concept to master: Learn to look at a piece of code and determine how its number of operations changes as the input grows. This is the foundation for analyzing algorithms and choosing efficient solutions.
