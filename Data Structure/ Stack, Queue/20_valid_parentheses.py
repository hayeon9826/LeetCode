class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}','[':']'}
        stack = []
        
        if len(s) % 2 == 1:
            return False
        
        for i in s:
            if i in dic:
                stack.append(dic[i])
            elif len(stack) > 0 and stack[len(stack)-1] == i:
                stack.pop()
            else: return False
        
        return len(stack) == 0
        

# REFERRENCE:
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            # if left parentheses, append to stack
            if char in dict.values():
                stack.append(char)
            # if right parentheses, check if the last element is same type of closing bracket
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

class Solution(object):
    def isValid(self, s):
          d = {'(':')', '{':'}','[':']'}
          stack = []
          for i in s:
              if i in d:  # 1
                  stack.append(i)
              elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                  return False
          return len(stack) == 0 # 3
    
# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket