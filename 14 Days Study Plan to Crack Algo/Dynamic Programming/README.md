# Dynamic Programming

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. For example, if we write simple recursive solution for Fibonacci Numbers, we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.

## Example: Fibonacci numbers

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

```python
Fn = Fn-1 + Fn-2
```

![fibo](https://media.geeksforgeeks.org/wp-content/cdn-uploads/program-for-fibonacci-numbers-1024x512.png)

Given a number n, print n-th Fibonacci Number.

Examples:

```python
Input  : n = 2
Output : 1

Input  : n = 9
Output : 34
```

### Dynamic Programming solution

```python
def fibonacci(n):

    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]


    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibonacci(9))
```

We can avoid the repeated work done in recursion by **storing the Fibonacci numbers** calculated so far.
