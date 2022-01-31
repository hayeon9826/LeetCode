class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()




# Source: https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation

# This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. 
# Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.

# If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. 
# If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. 
# If the white pointer is blue, we swap with the latest unclassified element.

def sortColors(self, nums):
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


# merge sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:

            # Finding the mid of the array
            mid = len(nums)//2
            # Dividing the array elements
            L = nums[:mid]
            # into 2 halves
            R = nums[mid:]
            # Sorting the first half
            self.sortColors(L)
            # Sorting the second half
            self.sortColors(R)
            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
  