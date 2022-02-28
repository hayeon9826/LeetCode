/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let dic = {};
  let answer = [];

  for (let word of strs) {
    let str = word.split("").sort().join("");
    if (str in dic) {
      answer[dic[str]].push(word);
    } else {
      dic[str] = answer.length;
      answer.push([word]);
    }
  }

  return answer;
};

// answer를 따로 선언하지 않고, 바로 dictionary의 값으로 넣어서 Objects.values로 가져오기
// https://leetcode.com/problems/group-anagrams/discuss/566236/Javascript-5-lines-explained
var groupAnagrams = function (strs) {
  let map = {};

  for (let str of strs) {
    let key = [...str].sort();
    map[key] = map[key] ? [...map[key], str] : [str];
  }

  return Object.values(map);
};
