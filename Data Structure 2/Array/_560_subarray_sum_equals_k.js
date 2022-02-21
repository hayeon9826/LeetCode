// Brute force
// timeout

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  var count = 0;
  for (start = 0; start < nums.length; start++) {
    for (end = start + 1; end <= nums.length; end++) {
      var sum = 0;
      for (i = start; i < end; i++) {
        sum = sum + nums[i];
      }
      if (sum == k) {
        count = count + 1;
      }
    }
  }
  return count;
};

// Approach 3: Without Space
// time limit exceeded

// Instead of considering all the startstart and endend points and then finding the sum for each subarray corresponding to those points,
// we can directly find the sum on the go while considering different endend points.
// i.e. We can choose a particular startstart point and while iterating over the endend points,
// we can add the element corresponding to the endend point to the sum formed till now.
//  Whenever the sum equals the required kk value, we can update the countcount value.
// We do so while iterating over all the endend indices possible for every startstart index. Whenever, we update the startstart index, we need to reset the sum value to 0.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  var count = 0;
  for (start = 0; start < nums.length; start++) {
    var sum = 0;
    for (end = start; end < nums.length; end++) {
      sum += nums[end];
      if (sum == k) {
        count = count + 1;
      }
    }
  }
  return count;
};

// The idea - Hash Map
// The key idea of how we can solve this problem in O(N) time using hashmap is to understand how we can correctly use the information from 1 iteration of calculating sums.

// Something to understand first is, when Sum_i = #0 + #1 + #2 .... + #i = 6, and Sum_k #0 + #1 + #2 ... + #k = 10,
// its pretty obvious that between #i to #k is equal to 4, and we can write that mathmatically to Sum_k - Sum_i = Sumi_to_k

// So In order to find k we are basically trying to find a pair of Sum_i and Sum_k such that Sum_k - Sum_i = k.
// Since we are only iterating the array once and calculating the sum from left to right accumatively, we can keep a record of all the sums up to index i,
//  that is Sum0, Sum1...Sumi. For each new sum, we can check if there is a previous Sum such that Sum_current - Sum_prev = k.
// In order to find what is the "old_index", we can just change the formula to Sum_curren - k = Sum_old and look up from our record to see if we find a matching pair.
// If we did, bingo, that means we found a valid subarray.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  var count = 0;
  var sum = 0;
  var map = new Map();
  map.set(0, 1);

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    // if map has pair of current cumulative sum, count the numers of pairs and add
    if (map.has(sum - k)) {
      count += map.get(sum - k);
    }
    // if map already has same key as current sum, add one value to that key. (b/c its duplicate)
    if (map.has(sum)) {
      map.set(sum, map.get(sum) + 1);
    } else {
      map.set(sum, 1);
    }
  }
  return count;
};
