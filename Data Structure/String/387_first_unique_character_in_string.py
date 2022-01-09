class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, string in enumerate(s):
            if not string in s[:index] + s[index+1:]:
                return index
        return -1
  
# dictionary
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = {}
        for string in s:
            if string in dictionary: 
              dictionary[string] += 1
            else: 
              dictionary[string] = 1
        for i in range(len(s)):
            if dictionary[s[i]] == 1: return i
        return -1