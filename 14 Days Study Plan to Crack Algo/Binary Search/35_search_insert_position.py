class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            # if 'mid' number is same as target, return position
            if target == nums[mid]:
                return mid
            # If target is smaller, ignore right half array
            elif target <  nums[mid]:
                end = mid - 1
            # If target is greater, ignore left half array
            else:
                start = mid + 1
        # if start is bigger than end, return start position
        return start