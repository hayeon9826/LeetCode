function solution(numbers, target) {
  let answer = 0;
  // dfs 정의. 만약 depth(총 갯수)를 끝까지 내려갔을 때 값이 target과 같으면 +1
  function dfs(depth, sum) {
    if (depth === numbers.length) {
      if (sum === target) {
        answer += 1;
      }
      return;
    }

    // 재귀
    dfs(depth + 1, sum + numbers[depth]); // dfs tree 왼쪽
    dfs(depth + 1, sum - numbers[depth]); // dfs tree 오른쪽
  }

  // dfs 시작
  dfs(0, 0);

  return answer;
}
