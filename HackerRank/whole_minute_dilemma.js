/*
 * Complete the 'playlist' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts INTEGER_ARRAY songs as parameter.
 */

function playlist(songs) {
  // Write your code here
  let remainder = Array(60).fill(0);
  let answer = 0;

  songs.forEach((value) => {
    remainder[value % 60]++;
  });

  for (let i = 1; i < 30; i++) {
    answer += remainder[i] * remainder[60 - i];
  }

  answer =
    answer +
    (remainder[30] * (remainder[30] - 1)) / 2 +
    (remainder[0] * (remainder[0] - 1)) / 2;

  return answer;
}

// question: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
