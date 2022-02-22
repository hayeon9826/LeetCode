/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */

var addStrings = function (num1, num2) {
  let i = num1.length - 1; // 맨뒤 인덱스를 잡음
  let j = num2.length - 1;
  let carry = 0;
  let sum = "";

  for (i, j; i >= 0 || j >= 0 || carry > 0; i--, j--) {
    // 뒷자리부터 하나씩 인덱싱
    const digit1 = i < 0 ? 0 : num1.charAt(i) - "0"; // 해단 index가 0보다 크다면, 해당 인덱스의 숫자를 찾아서
    const digit2 = j < 0 ? 0 : num2.charAt(j) - "0";
    const digitsSum = digit1 + digit2 + carry; // 더해준다. 이때 carry라는 올림수를 같이 올려줌
    sum = `${digitsSum % 10}${sum}`; // sum 이라는 변수에 위 세 변수 (digit1, digit2, carry) 의 합을 문자열로 나타냄
    carry = Math.floor(digitsSum / 10); // 그리고 올림수를 구해서 다음 합산시 더해줌
  }

  return sum;
};
