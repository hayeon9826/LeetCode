
# Other answer:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # x % y (remainder of x/y)
        # problem if k is larger than len(nums), thus calculate the remainder of k % len(nums)
        k = k % len(nums)
        # [:] is the array slice syntax for every element in the array.
        nums[:] = nums[-k:] + nums[:-k]

        # same as nums[:] = nums[length - k : length] + nums[:length - k]