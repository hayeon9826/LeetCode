class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            # if 'mid' number is same as target, return
            if nums[mid] == target:
                return mid
            # If target is smaller, ignore right half array
            elif nums[mid] > target:
                end = mid -1
            # If target is greater, ignore left half array
            elif nums[mid] < target:
                start = mid + 1
        # If we reach here, then the element was not present
        return -1