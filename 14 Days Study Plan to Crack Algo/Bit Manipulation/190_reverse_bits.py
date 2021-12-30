class Solution:
    def reverseBits(self, n: int) -> int:
      # {0:032b}.format(n) converts the integer to 32 bit binary representation.
      # int(binary_number, 2) turns binary to integer
        return int("{0:032b}".format(n)[::-1],2)
    
class Solution:
  def reverseBits(self, n: int) -> int:
      # bin(n) -> n to binary
      # bin(n)[:2] -> remove the 'b'
      # zfill(32) -> binary string of 32. fill 0s in front
      # [::-1] -> reverse the array
      # turn binary to integer
      return int(bin(n)[2:].zfill(32)[::-1], 2)