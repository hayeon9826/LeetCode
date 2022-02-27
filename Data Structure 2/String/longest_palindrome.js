/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  let dic = {};
  let sum = 0;
  let hasOne = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] in dic) {
      dic[s[i]]++;
    } else {
      dic[s[i]] = 1;
    }
  }

  if (Object.keys(dic).length == 1) {
    return s.length;
  } else {
    for (var key in dic) {
      if (dic[key] % 2 == 0) {
        sum += dic[key];
      } else {
        sum += dic[key] - 1;
        hasOne = 1;
      }
    }
    return sum + hasOne;
  }
};

// only one loop
// source: https://leetcode.com/problems/longest-palindrome/discuss/391018/JavaScript-solution-with-a-single-for-loop

var longestPalindrome = function (s) {
  let ans = 0;
  let keys = {};

  for (let char of s) {
    keys[char] = (keys[char] || 0) + 1;
    if (keys[char] % 2 == 0) ans += 2;
  }
  return s.length > ans ? ans + 1 : ans;
};

// source: https://leetcode.com/problems/longest-palindrome/discuss/791768/JavaScript-Solution

var longestPalindrome = function (s) {
  const set = new Set();
  let count = 0;

  for (const char of s) {
    if (set.has(char)) {
      count += 2;
      set.delete(char);
    } else {
      set.add(char);
    }
  }

  return count + (set.size > 0 ? 1 : 0);
};
