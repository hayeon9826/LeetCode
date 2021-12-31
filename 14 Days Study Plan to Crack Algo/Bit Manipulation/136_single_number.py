class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        #  make dictionary of numbers
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        # find number with value '1'
        for key, val in dic.items():
            if val == 1:
                return key



# bit manipulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
          # use XOR operator to find the single value
            answer ^= num
        return answer

# ^ (XOR)는 대응되는 비트가 서로 다르면 1을 반환함
# 즉, 0과 0이 아닌 수 a를 XOR로 연산하면 a가 나온다.
# 같은 숫자 끼리 XOR 연산하면 항상 0 이 나옴. 모든 자릿수가 같으니
# 따라서 하나 남은 숫자 값으로 반환됨