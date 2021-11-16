# Two Pointers

Two Pointers Algorithms is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

Below is an example of Two Pointers Algorithms

```python
A[] = {10, 20, 35, 50, 75, 80}
X = 70
i = 0
j = 5

A[i] + A[j] = 10 + 80 = 90
Since A[i] + A[j] > X, j--
i = 0
j = 4

A[i] + A[j] = 10 + 75 = 85
Since A[i] + A[j] > X, j--
i = 0
j = 3

A[i] + A[j] = 10 + 50 = 60
Since A[i] + A[j] < X, i++
i = 1
j = 3
m
A[i] + A[j] = 20 + 50 = 70
Thus this signifies that Pair is Found.
```

We start the sum of extreme values (smallest and largest) and conditionally move both pointers. We move left pointer ‘i’ when the sum of A[i] and A[j] is less than X. We do not miss any pair because the sum is already smaller than X. Same logic applies for right pointer j.

# Algorithms

There are two ways to solve this problem.

1. Naïve Approach using loops
2. Optimal approach using two pointer algorithm

### Naïve Approach

```python
# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum

# Method
def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            # as equal i and j means same element
            if(i == j):
                continue

            # pair exists
            if (A[i] + A[j] == X):
                return True

            # as the array is sorted
            if (A[i] + A[j] > X):
                break

    # No pair found with given sum
    return 0

# Driver code
arr = [3, 5, 9, 2, 8, 10, 11]
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9
```

Output: 1
Time Complexity: `O(n2)`

### Two Pointers Technique

```python
# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum
# Using Two-pointers Technique

# Method
def isPairSum(A, N, X):

    # represents first pointer
    i = 0

    # represents second pointer
    j = N - 1

    while(i < j):

        # If we find a pair
        if (A[i] + A[j] == X):
            return True

        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif(A[i] + A[j] < X):
            i += 1

        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return 0

# array declaration
arr = [3, 5, 9, 2, 8, 10, 11]

# value to search
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9.
```

Output: 1
Time Complexity: `O(n)`

<hr>

# Source
- [Two Pointers Technique(https://www.geeksforgeeks.org/two-pointers-technique/)
