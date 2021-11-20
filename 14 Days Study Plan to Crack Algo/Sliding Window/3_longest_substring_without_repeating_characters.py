class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        usedChar = {}
        maxLength = start = 0
        for index, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
            usedChar[char] = index

        print(usedChar)
        return maxLength

#### REFERENCE:


class Solution:
    """
        :type s: str
        :rtype: int
    """
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        for index,char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
	    usedChar[char] = index
        return maxLength


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

# source: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)