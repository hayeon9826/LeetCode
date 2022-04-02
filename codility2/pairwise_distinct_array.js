// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let sum = A.reduce((a, b) => a + b, 0);
  let max = [...Array(A.length + 1).keys()].reduce((a, b) => a + b, 0);

  return Math.abs(max - sum);
}

// reference: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
