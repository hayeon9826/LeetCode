function solution(numbers) {
  let answer = "";
  // 문자로 변환된 숫자를 연결하여 비교정렬
  answer = numbers
    .map((c) => c + "")
    .sort((a, b) => b + a - (a + b))
    .join("");

  // numbers 배열이 0으로만 구성되어 있을 경우 '0'만 출력
  return answer[0] === "0" ? "0" : answer;
}

// 참고: https://velog.io/@fastpace04/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4JavaScript-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98
