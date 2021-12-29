class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and not (n & (n - 1))
# if compare (power of 2) and (power of 2 - 1) with '&(AND)' operator, it always returns 0 because every number in each positions is different (whether 1 or 0)
# ex) 2: (10)2, 1: (1)2 -> (10)2 & (1)2  = 0
# ex) 4: (100)2, 3: (11)2 -> ...  = 0
# ex) 8: (1000)2, 7: (111)2 -> ...  = 0
# ex) 16: (10000)2, 15: (1111)2 -> ...  = 0



# AND ( & ): Bitwise AND is a binary operator that operates on two equal-length bit patterns. 
# If both bits in the compared position of the bit patterns are 1, the bit in the resulting bit pattern is 1, otherwise 0.
# A = 5 = (101)2 , B = 3 = (011)2 A & B = (101)2 & (011)2= (001)2 = 1