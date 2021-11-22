class Solution:

  #  time exceeded
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = ""
        start = 0
        
        for index, char in enumerate(s2):
            if s2[index] in s1:
                if(sorted(s2[index:index+len(s1)]) == sorted(s1)):
                    return True
            
        return False

# Success by using Counter runtime 8100 ms, memory 	14.3 MB
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = ""
        start = 0
        
        if(len(s1) > len(s2)):
            return False
        
        for index, char in enumerate(s2):
            if s2[index] in s1:
                if(Counter(s2[index:index+len(s1)]) == Counter(s1)):
                    return True
            
        return False


def checkInclusion(self, s1, s2):
    A = [ord(x) - ord('a') for x in s1]
    B = [ord(x) - ord('a') for x in s2]
    
    target = [0] * 26
    for x in A:
        target[x] += 1
    
    window = [0] * 26
    for i, x in enumerate(B):
        window[x] += 1
        if i >= len(A):
            window[B[i - len(A)]] -= 1
        if window == target:
            return True
    return False

# For each window representing a substring of s2 of length len(s1), we want to check if the count of the window is equal to the count of s1. 
# Here, the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]

# We can maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). 
# After, we only need to check if it is equal to the target. Working with list values of [0, 1,..., 25] instead of 'a'-'z' makes it easier to count later.

# Source: https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_frequency, windowStart, matched = {}, 0, 0
		
		# Intially add all the elements in the pattern into a hashmap along with their frequencies
        for letter in s1:
            if letter not in char_frequency:
                char_frequency[letter] = 0
            char_frequency[letter] += 1
        #
		# Now go through the pattern and if you find any letter which is also present in the hashmap
		# decrease the frequency and if the frequency is zero then there is a match
        for windowEnd in range(len(s2)):
            if s2[windowEnd] in char_frequency:
                char_frequency[s2[windowEnd]] -= 1
                if char_frequency[s2[windowEnd]] == 0:
                    matched += 1
            #If the number of matches is equal to number if letters in the pattern then return True
            if matched == len(char_frequency):
                return True
            
			# Intially when you reach to the point where length of the pattern is equals to and greater than length of the string,  then consider the windowStart. If it is present in the hashmap decrease the  frequency and slide the window i.e., increment the windowStart 
            if windowEnd >= len(s1) - 1:
                if s2[windowStart] in char_frequency:
                    if char_frequency[s2[windowStart]] == 0:
					#If the frequency is equal to zero then decrement the match
                        matched -= 1
                    char_frequency[s2[windowStart]] += 1
                windowStart += 1
        return False

# Source: https://leetcode.com/problems/permutation-in-string/discuss/312518/Easy-to-understand-python-solution




class Solution:
    def checkInclusion(self, s1, s2):
	# 102 / 102 test cases passed.
	# Status: Accepted
	# Runtime: 64 ms
        ls1 = len(s1)
        key = sum(map(hash, s1))
        now = sum(map(hash, s2[:ls1]))
        if key == now: return True
        for i in range(ls1, len(s2)):
            now = now - hash(s2[i - ls1]) + hash(s2[i])
            if now == key:
                return True
        return False

# For counter solution, we need to compare each count for each letter, so the time complesity is not O(n) but O(n * len(set(s1))).
# If using the hash function to generate the key for comparision, the time complesity will be true O(n)git

# Source: https://leetcode.com/problems/permutation-in-string/discuss/173045/Short-97-Python-NO-Counter