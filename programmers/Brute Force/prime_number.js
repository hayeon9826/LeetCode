function solution(numbers) {
  let answer = 0;
  let nums = numbers.split("");
  // 중복 숫자 없애기 위해 set 사용
  let set = new Set();
  dfs(set, nums, "");

  return set.size;
}

// dfs로 모든 순열의 수 구하기
function dfs(set, arr, fixed) {
  if (arr.length >= 1) {
    for (let i = 0; i < arr.length; i++) {
      let newFixed = fixed + arr[i];
      let copyArr = [...arr];
      copyArr.splice(i, 1);

      if (isPrime(parseInt(newFixed))) {
        set.add(parseInt(newFixed));
      }

      dfs(set, copyArr, newFixed);
    }
  }
}

// 소수 인지 체크
function isPrime(number) {
  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      return false;
    }
  }

  return number > 1;
}
