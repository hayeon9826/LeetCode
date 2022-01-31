
# source
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                # to avoid dup triplets
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[j] + nums[k]
                if s < -nums[i]:
                    j+=1
                elif s > -nums[i]:
                    k-=1
                else:
                    trips.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # below 2 loops to avoid dup triplets
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
        return trips


# 작성중인 코드
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        
        if len(nums) < 3:
            return answer
        elif nums[0] * nums[len(nums)-1] > 0:
            return answer
        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]
        else:
            for i in range(int(len(nums)/2)):
                start, end = nums[i], nums[-(i+1)]
                if -(start+end) in nums:
                    answer.append([start, end, -(start+end)])
        return answer