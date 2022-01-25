class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        # Bitwise operation
        # 1 xor 1 gives 0. 2 xor 2 gives 0
        # what it means 1 xor 1, 2 xor 2, 3 xor 3 will always give you 0
        # [4,1,2,1,2] - > [4] will stay as 4 [1,2,1,2] will cancel each other. 
        # T: O(N)
        # S: O(1)
        for num in nums:
            answer ^= num
        return answer



# source: https://leetcode.com/problems/single-number/discuss/1216856/Python-Solutions
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Brute force version
        # T: O(N)
        # S: O(N)
        
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for k,v in d.items():
            if v == 1:
                return k


    def singleNumber(self, nums: List[int]) -> int:
        
        # Brute force version 2.0, Using python library to build dictionary
        # T: O(N)
        # S: O(N)
        
        d = Counter(nums)
        
        for k,v in d.items():
            if v == 1:
                return k