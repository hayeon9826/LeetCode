// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  let count_arr = [];
  let current_word = S[0];
  let current_count = 0;
  for (let i = 0; i < S.length + 1; i++) {
    if (S[i] == current_word) {
      current_count += 1;
    } else {
      count_arr.push(current_count);
      current_count = 1;
      current_word = S[i];
    }
  }

  count_arr.sort((a, b) => b - a);

  return count_arr[0] * count_arr.length - S.length;
}
