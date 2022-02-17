/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let answer = [];
  for (i = 0; i < nums.length; i++) {
    let value = nums.reduce(
      (total, val, idx) => (idx == i ? total : total * val),
      1
    );
    answer.push(value);
  }

  return answer;
};

var productExceptSelf = function (nums) {
  const result = [];
  let productSoFar = 1;
  for (let i = 0; i < nums.length; i++) {
    result[i] = productSoFar;
    productSoFar *= nums[i];
  }

  productSoFar = 1;
  for (let j = nums.length - 1; j >= 0; j--) {
    result[j] *= productSoFar;
    productSoFar *= nums[j];
  }

  return result;
};
