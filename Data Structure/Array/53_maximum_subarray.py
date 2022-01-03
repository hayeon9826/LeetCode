class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = maxSum = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            maxSum = max(maxSum, current)

        return maxSum