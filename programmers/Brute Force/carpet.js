function solution(brown, yellow) {
  let answer;
  let samples = [];

  // x, y 좌표를 모두 구함. 단, x의 크기가 y보다 커야함
  for (let i = brown + yellow; i > 0; i--) {
    if (i ^ (2 >= brown + yellow) && (brown + yellow) % i == 0) {
      if ((brown + yellow) / i > i) {
        break;
      }
      samples.push([i, (brown + yellow) / i]);
    }
  }

  // 구한 좌표들을 하나씩 비교해가며 해를 구함
  for (let i = 0; i < samples.length; i++) {
    if (samples[i][0] + samples[i][1] == (brown + 4) / 2) {
      answer = samples[i];
    }
  }

  return answer;
}
