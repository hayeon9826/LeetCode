# LeetCode Algorithms

[리트코드](https://leetcode.com/)에서 알고리즘 및 자료구조 문제를 푸는 깃헙입니다. 주로 파이썬을 사용할 예정이며, 문제와 함께 개념 / 답안 / 참고한 링크들을 표시합니다.


각 주제마다 README.md 파일에서 알고리즘 개념을 설명합니다. (Geeks for Geeks 등 타 사이트 참고) 


Question.md 파일에는 주제별 알고리즘 문제가 적혀있습니다.



# Algorithms

### 14 Days Study Plan to Crack Algo [[link](https://leetcode.com/study-plan/algorithm/)]
- [Binary Search](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Binary%20Search) - 이진 탐색이란 정렬된 배열에서 특정 값을 찾는 알고리즘이다. 배열의 중간에 있는 값을 선택해 찾고자 하는 값 A와 비교한다. A가 중간 값보다 작으면 배열 좌측의 값들을, A가 중간값보다 배열의 우측의 값들을 탐색한다. 그리고 해당 값을 찾을 때까지 이 과정을 반복한다. `시간 복잡도: O(logN)`

- [Two Pointers](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Two%20Pointers) - 투 포인터 알고리즘은 정렬된 리스트와 두 개의 포인터를 이용한 알고리즘이다. 두 개의 포인터로 타겟값에 순차적으로 접근하면서, 두 포인터 구간의 값이 타겟 값과 같을 때 까지 포인터를 조작하는 기법을 말한다.  `시간 복잡도:  O(n)`


- [Sliding Window](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Sliding%20Window) - 슬라이딩 윈도우(Sliding Window) 알고리즘은 고정된 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 푸는 알고리즘을 이다. 배열이나 리스트의 요소의 일정 범위의 값을 비교할때 사용하면 좋은 알고리즘이다. 투 포인터와 개념이 비슷한데, 두 포인터 간의 거리가 고정되어있다는 점에서 차이가 있다. 예를 들어 정수로 이루어진 배열 [1, 2, 6, 4, 8, 6, 3, 9, 3] 에서 길이가 3인 서브배열의 합계가 가장 큰 배열을 푸는 문제에서 사용될 수 있다.  `시간 복잡도:  O(n)`


- [Breadth-First Search / Depth-First Search](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Breadth-First%20Search%2C%20Depth-First%20Search) - 너비 우선 탐색(BFS)과 깊이 우선 탐색(DFS) 알고리즘이다. 두 가지 모두 그래프를 탐색하는 방법이다. 그래프란 정점(node)과 그 정점을 연결하는 간선(edge)으로 이루어진 자료구조를 말하며, 하나의 정점에서 시작해 차례대로 모든 정점들을 한 번씩 방문하는 것을 말한다.

- BFS(너비우선탐색): 현재 정점에 연결된 가까운 점들부터 탐색 / 큐를 이용해서 구현
> BFS의 시간복잡도: 인접 리스트로 표현된 그래프 - `O(N+E)` / 인접 행렬로 표현된 그래프 - `O(N^2)`

- DFS(깊이우선탐색): 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색 / 스택 또는 재귀함수로 구현
> DFS의 시간복잡도: 인접 리스트로 표현된 그래프 - `O(N+E)` / 인접 행렬로 표현된 그래프 - `O(N^2)`

- 경로의 특징을 저장해둬야 하는 문제는 DFS가 유리하며, 최단거리를 구해야 할 경우 BFS가 유리
	




- [Recursion / Backtracking](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Recursion%2C%20Backtracking) - 재귀 함수는 자기 자신을 참조하는 함수이다. 원래의 문제를 동일한 유형의 하위 문제로 나누고 하위문제를 해결한 다음 결과와 결합한다. (시간 복잡도 `O(n2)`) 백트래킹은 한정 조건을 가진 문제를 푸는 전략이다. 해를 찾는 도중 해당 경로에서 해가 나오지 않고 막히면, 되돌아가서 다른 경로에서 해를 찾아가는 기법을 말한다. (시간 복잡도는 ` O(N!)`)


- [Dynamic Programming](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Dynamic%20Programming) - 동적 프로그래밍은 분할정복 기법으로 문제를 푸는것. (기억하는 프로그래밍) 큰 문제를 한 번에 해결하기 힘들 때 작은 여러 개의 문제로 나누어서 푸는 기법이다. 작은 문제들을 풀다보면 같은 문제들을 반복해서 푸는 경우가 생기는데, 그 문제들을 매번 재계산하지 않고 값을 저장해두었다가 재사용하는 기법이 동적 프로그래밍이다. 시간 복잡도는 `O(N)`
-  재귀 호출 시 반복적으로 계산되는 것들의 계산 횟수를 줄이기 위해 이전에 계산했던 값을 저장해두었다가 나중에 재사용하는 **메모이제이션**이 동적 프로그래밍 중 하나임


- [Bit Manipulation](https://github.com/hayeon9826/LeetCode/tree/main/14%20Days%20Study%20Plan%20to%20Crack%20Algo/Bit%20Manipulation)
