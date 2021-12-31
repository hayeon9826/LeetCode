class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums의 set(중복제거)와 nums 길이 비교
        return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            nums[1:]
            if i in nums:
                return True
        return False