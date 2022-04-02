// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  if (K > A.length || A.length == 0) {
    return -1;
  }

  if (K == A.length) {
    return A.reduce((a, b) => a + b) % 2 == 0 ? A.reduce((a, b) => a + b) : -1;
  }

  A.sort((a, b) => b - a);

  even = [];
  odd = [];
  even_count = 0;
  odd_count = 0;
  max = 0;

  for (let i = 0; i < A.length; i++) {
    if (A[i] % 2 == 0) {
      even.push(A[i]);
    } else {
      odd.push(A[i]);
    }
  }

  while (K > 0) {
    if (K % 2 == 1) {
      if (even.length > 0) {
        max += even[even_count];
        even_count += 1;
        K -= 1;
      } else {
        return -1;
      }
    } else {
      if (even_count < even.length - 1 && odd_count < odd.length - 1) {
        max += Math.max(
          even[even_count] + even[even_count + 1],
          odd[odd_count] + odd[odd_count + 1]
        );
        even_count += 2;
        odd_count += 2;
      } else if (even_count < even.length - 1) {
        max += even[even_count] + even[even_count + 1];
        even_count += 2;
      } else if (odd_count < odd.length - 1) {
        max += odd[odd_count] + odd[odd_count + 1];
        odd_count += 2;
      }
      K -= 2;
    }
  }

  return max;
}

// Question: https://levelup.gitconnected.com/maximum-even-sum-of-k-elements-ca060ab3a9fd
