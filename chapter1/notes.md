# Chapter 1: Why Data Structures Matter — Summary Notes

## 1. Arrays vs. Array-Based Sets

- Array: Stores values in an ordered sequence and allows duplicates.
- Array-based set: Stores values in an array-like structure but does not allow duplicates.

Example:

```
# Array — duplicates allowedfruits = ["apple", "banana", "apple"]# Array-based set — uniqueness must be enforcedfruits = ["apple", "banana"]
```

## 2. Understanding N

\\(N\\) represents the number of elements in a data structure.

For example, if a list contains 100 elements, \\(N = 100\\).

## 3. Operations and Their Step Counts

| Operation                     | Array | Array-based set |
| ----------------------------- | ----- | --------------- |
| Reading by index              | 1     | 1               |
| Searching for a missing value | N     | N               |
| Insertion at beginning        | N + 1 | 2N + 1          |
| Insertion at end              | 1     | N + 1           |
| Deletion at beginning         | N     | N               |
| Deletion at end               | 1     | 1               |

These are the book's simplified step counts.

## 4. Why Set Insertion Takes More Steps

An array-based set must check whether a value already exists before inserting it.

### Insertion at the end

Suppose the set contains five elements:

Initial set (N = 5)

apples

bananas

cucumbers

dates

elderberries

Search all 5 elements to ensure `"figs"` is not already present.

Insert `"figs"` at the end: 1 step.

Total: \\(N+1=5+1=\mathbf{6}\\) steps.

### Insertion at the beginning

The set must search for duplicates, shift all existing elements to the right, and then insert the new value.

\\[ N+N+1=2N+1 \\]

For \\(N=100\\):

\\[ 100+100+1=\boxed{201\text{ steps}} \\]

## 5. Linear Search

Linear search checks elements one at a time until it finds the target.

```
def linear_search(items, target):    for index, item in enumerate(items):        if item == target:            return index    return -1
```

- Best case: 1 step, if the first element matches.
- Worst case: \\(N\\) steps, if the target is last or absent.
- Finding every occurrence requires checking all \\(N\\) elements.

## 6. Why Choosing a Data Structure Matters

- Use an array when you need ordered values and efficient insertion at the end, and duplicates are acceptable.
- Use an array-based set when preventing duplicate values is important, accepting the extra search required for insertion.

Remember: The best data structure depends on what your application needs. Code that works is important, but understanding how many steps it takes helps you write efficient code.
