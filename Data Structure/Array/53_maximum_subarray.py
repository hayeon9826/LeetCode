# dp
# 이어지는 배열의 값을 이전 합과 비교해나가며 max 값을 기록
# maxSum 변수에는 비교해나간 max 값 중 최댓값 구하기
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = maxSum = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            maxSum = max(maxSum, current)

        return maxSum
#dp
# maxSum 숫자 변수 없이, 배열로 직접 비교하고 값을 저장함
# 마지막에 해당 배열에서 최댓값 구하기 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums
        for i in range(1, len(nums)):
            current[i] = max(current[i], current[i] + current[i-1])
        return max(current)


# print 한 결과:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums
        for i in range(1, len(nums)):
            current[i] = max(current[i], current[i] + current[i-1])
            print(current)
        return max(current)
# input:  [-2,1,-3,4,-1,2,1,-5,4]
# result: 
  # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  # [-2, 1, -2, 4, -1, 2, 1, -5, 4]
  # [-2, 1, -2, 4, -1, 2, 1, -5, 4]
  # [-2, 1, -2, 4, 3, 2, 1, -5, 4]
  # [-2, 1, -2, 4, 3, 5, 1, -5, 4]
  # [-2, 1, -2, 4, 3, 5, 6, -5, 4]
  # [-2, 1, -2, 4, 3, 5, 6, 1, 4]
  # [-2, 1, -2, 4, 3, 5, 6, 1, 5]

# answer: 6