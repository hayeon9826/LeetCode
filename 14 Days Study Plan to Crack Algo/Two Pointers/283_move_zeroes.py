class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            #if nums[i] value is 0
            if nums[i] == 0:
                #remove the item (0)
                nums.remove(0)
                # and add 0 at the end of the list
                nums.insert(len(nums), 0)




# faster solutions
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)
        while start < end:
            if nums[start]!=0:
                start +=1
            else:
                nums.append(nums.pop(start))
                end -= 1