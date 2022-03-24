function balancedSum(arr) {
  // Write your code here
  let sum = arr.reduce((a, b) => a + b, 0);
  let partial = arr[0];

  for (let i = 1; i < arr.length - 1; i++) {
    if (partial == sum - partial - arr[i]) {
      return i;
    }
    partial += arr[i];
  }
}

// question: https://www.hackerrank.com/contests/world-codesprint-11/challenges/balanced-array
