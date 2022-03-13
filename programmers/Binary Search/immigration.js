function solution(n, times) {
  times.sort((a, b) => a - b); // 시간을 오름차순으로 정렬

  let max = times[times.length - 1] * n; // 최대시간 기준값
  let min = 0; // 기준값
  let mid = Math.floor((max + min) / 2);

  while (min <= max) {
    let count = 0;

    for (let time of times) {
      count += Math.floor(mid / time); // 한 사람당 몇명 할 수 있는지
    }

    if (count >= n) {
      max = mid - 1;
    } else {
      min = mid + 1;
    }

    mid = Math.floor((max + min) / 2);
  }

  return min;
}

// times를 오름차순으로 정렬시킨다.
// 가장 늦게 끝나는 시간을 구한다
// 가장 오래걸리는 심사대 * n
// 이분탐색으로 해당 시간에 각 심사대의 최대 심사 수의 합 인 count 를 구한다.
// count >= n 인 경우
// 최솟값을 갱신한다.
// mid의 왼쪽을 탐색한다.
// right = mid-1;
// count < n 인 경우
// mid의 오른쪽을 탐색한다.
// left = mid+1
