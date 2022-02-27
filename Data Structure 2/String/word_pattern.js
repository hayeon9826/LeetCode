/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function (pattern, s) {
  let arr = s.split(" ");
  let dic = {};

  if (arr.length !== pattern.length) {
    return false;
  }

  for (let i = 0; i < pattern.length; i++) {
    if (pattern[i] in dic) {
      if (dic[pattern[i]] !== arr[i]) {
        return false;
      }
    } else {
      if (Object.values(dic).includes(arr[i])) {
        return false;
      } else {
        dic[pattern[i]] = arr[i];
      }
    }
  }

  return true;
};

// js clean solution
// source: https://leetcode.com/problems/word-pattern/discuss/834256/JavaScript-Clean-Solution
var wordPattern = function (pattern, str) {
  const words = str.split(/\s+/);
  const map = new Map();

  if (words.length !== pattern.length) return false;
  if (new Set(words).size !== new Set(pattern).size) return false;

  for (let i = 0; i < pattern.length; i++) {
    if (map.has(pattern[i]) && map.get(pattern[i]) !== words[i]) return false;
    map.set(pattern[i], words[i]);
  }
  return true;
};
