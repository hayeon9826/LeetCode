
# Other answer:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # x % y (remainder of x/y)
        k = k % len(nums)
        # [:] is the array slice syntax for every element in the array.
        nums[:] = nums[-k:] + nums[:-k]