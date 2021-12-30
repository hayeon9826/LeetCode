# build in library

def hammingWeight(self, n):
  # convert n to binary and count '1's
    return bin(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            # 가장 우측의 bit 1을 없앰
            n = n & (n - 1)
            c += 1
        return c

# 설명

# n & (n - 1) drops the lowest set bit. It's a neat little bit trick.

# Let's use n = 00101100 as an example. This binary representation has three 1s.

# If n = 00101100, then n - 1 = 00101011, so n & (n - 1) = 00101100 & 00101011 = 00101000. Count = 1.

# If n = 00101000, then n - 1 = 00100111, so n & (n - 1) = 00101000 & 00100111 = 00100000. Count = 2.

# If n = 00100000, then n - 1 = 00011111, so n & (n - 1) = 00100000 & 00011111 = 00000000. Count = 3.

# n is now zero, so the while loop ends, and the final count (the numbers of set bits) is returned.