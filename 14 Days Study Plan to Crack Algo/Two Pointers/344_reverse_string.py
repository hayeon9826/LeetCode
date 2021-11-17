class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # define i as start point (first index 0) and j as end point (last index)
        i = 0
        j = len(s) - 1
        # until start point is smaller than end point
        while(i < j): 
            # swap first - end elements
            s[i], s[j] = s[j], s[i]
            # move two points towards middle by 1
            i += 1
            j -= 1




# the PYTHONIC way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# using the array extended slice
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[::-1]

# * https://docs.python.org/release/2.3.5/whatsnew/section-slices.html