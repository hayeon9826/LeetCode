class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
  

# using dictionary (better solution)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for char in t:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True
# Runtime: 54 ms, faster than 46.38% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 81.48% of Python3 online submissions for Valid Anagram.