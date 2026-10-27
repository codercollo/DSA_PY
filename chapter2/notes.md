# Chapter 2: Why Algorithms Matter

_Based on A Common-Sense Guide to Data Structures and Algorithms — Jay Wengrow_

## 1. What Is an Algorithm?

An **algorithm** is a set of instructions for completing a specific task.

Examples:

- Searching for a number in an array.
- Sorting a list of values.
- Finding a user's account in a database.

Different algorithms can solve the same problem but require different numbers of steps. Choosing the right algorithm affects performance, especially as the amount of data increases.

**Key idea:** The data structure and the algorithm you choose both influence efficiency.

---

## 2. Ordered Arrays

An **ordered array** is an array whose elements are always maintained in sorted order.

Example:

```python
numbers = [3, 17, 80, 202]
```

If we insert `75`, the result must be:

```python
[3, 17, 75, 80, 202]
```

Unlike a regular array, we cannot simply append `75` and leave the values unsorted.

### How insertion works

Starting array:

```text
[3, 17, 80, 202]
```

1. Compare `75` with `3`: move right.
2. Compare `75` with `17`: move right.
3. Compare `75` with `80`: insert before `80`.
4. Shift `202` one position right.
5. Shift `80` one position right.
6. Insert `75`.

Result:

```text
[3, 17, 75, 80, 202]
```

Insertion requires:

- **Comparisons** to find the correct position.
- **Shifts** to make room.
- An insertion operation to place the value.

For an array with \(N\) existing elements, insertion can take up to a linear number of steps, depending on where the value belongs. In the book's example, inserting `75` into four elements takes six steps.

**Trade-off:** Ordered arrays make searching more efficient, but insertion can be slower because values may need to be shifted.

---

## 3. Linear Search

**Linear search** checks elements one at a time until the target is found or the search ends.

Example:

```python
numbers = [3, 17, 75, 80, 202]
target = 75

for index, number in enumerate(numbers):
    if number == target:
        print("Found at index:", index)
        break
```

Illustration — searching for `75`:

```text
[3] → [17] → [75] → [80] → [202]
 1      2      3
             FOUND
```

The algorithm makes three comparisons.

### Linear search in an ordered array

An ordered array allows us to stop early when we encounter a number greater than the target.

```python
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
        elif number > target:
            return None

    return None
```

For example, searching for `22` in:

```text
[3, 17, 75, 80, 202]
```

We check `3`, `17`, and `75`. Since `75 > 22`, we know `22` cannot appear later in the array.

A regular, unordered array cannot safely use this early-stop rule.

**Worst-case performance:** Linear search can require \(N\) comparisons for \(N\) elements.

---

## 4. Binary Search

**Binary search** is a searching algorithm that repeatedly halves the remaining search space.

**Requirement:** The array must be sorted.

Imagine guessing a number between 1 and 100. Guessing 50 first is more efficient than starting at 1 because the first guess eliminates roughly half the possibilities.

### How it works

1. Set the lower and upper search boundaries.
2. Calculate the middle index.
3. Compare the middle element with the target.
4. If they match, return the result.
5. If the target is smaller, search the left half.
6. If the target is larger, search the right half.
7. Repeat until the target is found or no candidates remain.

### Python implementation

```python
def binary_search(numbers, target):
    first = 0
    last = len(numbers) - 1

    while first <= last:
        mid = (first + last) // 2
        middle_value = numbers[mid]

        if middle_value == target:
            return mid
        elif target < middle_value:
            last = mid - 1
        else:
            first = mid + 1

    return None
```

Example:

```python
numbers = [2, 4, 6, 8, 10, 12, 13]

print(binary_search(numbers, 8))
# 3
```

The result is index `3`, because Python indexes start at zero.

### Illustration: searching for 8

```text
Index:   0  1  2  3  4   5   6
Array:  [2, 4, 6, 8, 10, 12, 13]
                  ↑
             Middle value
```

The middle index is:

```python
mid = (0 + 6) // 2  # 3
```

The element at that index is `8`, so the target is found in **one comparison**.

### Important implementation details

- `first` and `last` represent indexes, not element values.
- `numbers[mid]` retrieves the middle element.
- `//` performs integer division in Python.
- `last = mid - 1` eliminates the middle and everything to its right.
- `first = mid + 1` eliminates the middle and everything to its left.
- `while first <= last` continues while possible candidates remain.
- If the loop ends without finding the target, return `None`.

---

## 5. Binary Search vs. Linear Search

| Array size | Linear search — maximum comparisons | Binary search — maximum comparisons |
| ---------: | ----------------------------------: | ----------------------------------: |
|          3 |                                   3 |                                   2 |
|          7 |                                   7 |                                   3 |
|        100 |                                 100 |                                   7 |
|     10,000 |                              10,000 |                                  14 |
|    100,000 |                             100,000 |                                  17 |
|  1,000,000 |                           1,000,000 |                                  20 |

The book gives 13 maximum steps for 10,000 elements; the exact maximum under the comparison-counting convention used in our Python implementation is 14.

### Why is binary search faster?

Linear search removes one candidate per unsuccessful comparison.

```text
100 elements → potentially 100 comparisons
```

Binary search removes approximately half the remaining candidates per comparison.

```text
100,000 elements
        ↓
     50,000
        ↓
     25,000
        ↓
       ...
        ↓
   1 candidate
```

Each time the dataset doubles, binary search needs only about one additional comparison.

---

## 6. Counting Steps Correctly

When learning algorithms, define what counts as a step. For searching, counting each comparison with an array element is a useful convention.

### Linear search example

```python
def linear_search(target):
    numbers = [2, 4, 6, 8, 10, 12, 13]
    steps = 0

    for number in numbers:
        steps += 1

        if number == target:
            print("Found:", number)
            print("Steps:", steps)
            return

    print("Not found")
    print("Steps:", steps)
```

Searching for `8` requires four comparisons: `2`, `4`, `6`, then `8`.

### Binary search example

```python
def binary_search(target):
    numbers = list(range(100000))
    first = 0
    last = len(numbers) - 1
    steps = 0

    while first <= last:
        mid = (first + last) // 2
        steps += 1

        if numbers[mid] == target:
            print("Found:", target)
            print("Steps:", steps)
            return
        elif target < numbers[mid]:
            last = mid - 1
        else:
            first = mid + 1

    print("Not found:", target)
    print("Steps:", steps)
```

```python
binary_search(47)       # Finds 47 in 11 comparisons.
binary_search(100000)   # Target is absent; takes 17 comparisons.
```

The second call demonstrates the maximum for this array under this implementation.

---

## 7. Choosing the Right Approach

There is no single data structure or algorithm that is best for every situation.

| Situation                                             | Suitable choice                    |
| ----------------------------------------------------- | ---------------------------------- |
| Data is unsorted and you need to search it            | Linear search                      |
| Data is sorted and you need efficient searching       | Binary search                      |
| Data is frequently inserted and searching is uncommon | A regular array may be preferable  |
| Data is searched frequently and kept sorted           | An ordered array may be worthwhile |

Remember that keeping an array sorted has a cost: insertion may require searching for the correct position and shifting elements.

## 8. Key Takeaways

- An algorithm is a set of instructions for solving a task.
- Different algorithms can solve the same problem with different efficiency.
- Ordered arrays maintain their values in sorted order.
- Inserting into an ordered array can require comparisons and shifts.
- Linear search examines elements sequentially.
- Binary search repeatedly halves the search space and requires sorted data.
- Linear search has worst-case \(O(N)\) time complexity.
- Binary search has worst-case \(O(\log N)\) time complexity.
- Count comparisons consistently when comparing these searching algorithms.
- Choose data structures and algorithms according to the operations your application performs most often.

**Chapter summary:** The main lesson is not simply to choose binary search over linear search. It is to understand the trade-offs and select the approach that fits the data and the problem.
