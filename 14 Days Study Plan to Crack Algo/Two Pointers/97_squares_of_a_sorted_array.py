class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # square each element in array
            nums[i] =  nums[i] *  nums[i]
        # sort the squared array
        nums.sort()
        
        return nums