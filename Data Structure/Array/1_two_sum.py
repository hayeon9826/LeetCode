
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
          # 본인 값 제외하고, 나머지 배열에 짝이 되는 수가 있다면
            if (target - nums[i]) in nums[i+1:]:
              # 본인 index와 짝인 수의 index 리턴
                return[i, nums[i+1:].index(target - nums[i]) + i + 1]



# dictionary 활용
# 각 배열의 값과 index를 저장하며, 짝의 수가 있는지 확인
    def twoSum(self, nums, target):
        dic = {}
        for i, val in enumerate(nums):
            ans = target - val
            if ans in dic:
                return [dic[ans], i]
            else:
                dic[val] = i