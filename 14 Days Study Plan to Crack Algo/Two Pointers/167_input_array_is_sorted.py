class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        # two pointers start at the end of the array (first index, last index)
        
        while i < j:
            # if the sum is same as target, return index + 1
            if numbers[i] + numbers[j] == target:
                return[ i+1, j+1 ]
            # if the sum is bigger than the target, last index -1
            # since the array is in ascending order
            elif numbers[i] + numbers[j] > target:
                j -= 1
            # if the sum is smaller than the target, first index + 1
            else:
                i += 1