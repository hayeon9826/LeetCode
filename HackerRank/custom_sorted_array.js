function moves(arr) {
  // Write your code here
  let evenCheck = new Array(arr.length).fill(0);
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      evenCheck[i] = 1;
      sum++;
    }
  }

  let answer = 0;

  for (let i = 0; i < sum; i++) {
    if (evenCheck[i] == 0) {
      answer++;
    }
  }

  return answer;
}

// question: https://stoilsky.com/js-array-performance/
