# using array

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        duplicates = []
        for num in nums1:
            if num in nums2:
                duplicates.append(num)
                nums2.remove(num)
        
        return duplicates

# Runtime: 60 ms, faster than 33.80% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.5 MB, less than 43.86% of Python3 online submissions for Intersection of Two Arrays II.

# using dictionary
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        for i in nums1:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        duplicates = []
        for i in nums2:
            if i in dictionary and dictionary[i]>0:
                duplicates.append(i)
                dictionary[i] -= 1
        return duplicates

# Runtime: 46 ms, faster than 68.73% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.4 MB, less than 43.86% of Python3 online submissions for Intersection of Two Arrays II.
