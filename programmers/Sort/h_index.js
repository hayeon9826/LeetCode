function solution(citations) {
  let answer = 0;
  citations.sort((a, b) => b - a);

  for (let i = 0; i < citations.length; i++) {
    if (i < citations[i]) {
      answer++;
    }
  }
  return answer;
}

// source: https://laycoder.tistory.com/211

// 논문 인용횟수를 내림차순으로 정렬하고 배열 길이만큼 for문을 돌린다.
// 자신의 인용횟수(citations[i])가 자신보다 인용횟수가 많은 논문 수(i) 보다 많으면 정답 수를 1 증가시킨다.
// 자신의 인용횟수가 자신보다 인용횟수가 많은 논문 수와 같아 질때 의 answer를 return하면 정답이다.
