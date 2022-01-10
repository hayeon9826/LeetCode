class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = "".join(sorted(ransomNote))
        magazine = "".join(sorted(magazine))
        
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, "", 1)
            else:
                return False
        return True


# Faster
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if magazine.count(char) < ransomNote.count(char):
                return False
        return True
        
# Runtime: 36 ms, faster than 95.60% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.5 MB, less than 9.62% of Python3 online submissions for Ransom Note.