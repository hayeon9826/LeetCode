class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums의 set(중복제거)와 nums 길이 비교
        return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      # sore the array
        nums.sort()
        for i in range(1,len(nums)):
          # 연속적인 수 중에 같은 수 있는지 체크
            if nums[i] == nums[i-1]:
                return True
        return False
        # O(n)