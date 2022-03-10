function solution(n, computers) {
  let answer = 0,
    visited = [];

  for (let i = 0; i < computers.length; i++) {
    if (!visited[i]) {
      answer += 1;
      dfs(i, computers, visited);
    }
  }

  return answer;
}

function dfs(start, computers, visited) {
  visited[start] = 1;
  for (let i = 0; i < computers.length; i++) {
    if (!visited[i] && computers[start][i]) {
      dfs(i, computers, visited);
    }
  }
}

// 1. DFS 재귀 함수를 이용해서 접근. 각각의 컴퓨터를 노드로 인식함
// 2. 우선 정답의 갯수를 저장할 변수, 방문할 노드를 담은 배열이 필요함
// 3. 처음에 방문한 배열 (visit)은 빈 배열, 정답은 0에서 시작
// 4. i = 0에서 n까지 for 문을 돌리면서, 만약 i 번째 자리에 방문 배열 값이 없다면, 정답을 +1 해주고, dfs (dfs 방식으로 연결된 네트워크를 찾는 방식) 함수를 호출한다.
// 5. *정답을 +1 해주는 이유는 그 노드 부터 이어진 네트워크를 탐색한다는 뜻임
// 6. dfs 함수로 다시 for문을 돌리는데, 만약 방문하지 않았는데 1이 표시된 컴퓨터를 만나면 dfs를 다시 호출해줌 (→ 이 경우, answer를 늘리지 않고 방문 배열만 체크할 수 있기 때문)
// 7. dfs가 다 돌아가면 다시 원래 for문으로 돌아가서 방문 배열에 없는 index 찾으면 정답 + 1 해주도 또 다른 네트워크 찾으러 dfs 돌려줌 (기존의 네트워크 하나 찾았고, 새로운 네트워크를 찾으러 가는 것임)
