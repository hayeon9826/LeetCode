
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        # until start <= end
        while start <= end:
            mid = (start + end) // 2
            # if badVersion(mid) is true
            if isBadVersion(mid):
                # return mid if badVersion(mid - 1) is false
                if isBadVersion(mid - 1) == False:
                    return mid
                # if mid & mid -1 are both true, remove the right half of the array 
                else:
                    end = mid - 1
            # if badVersion(mid) is false, remove the left half the array
            else:
                start = mid + 1
        return start