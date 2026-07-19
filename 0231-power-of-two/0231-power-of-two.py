class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
          #  return n > 0 and (n & (n - 1)) == 0
        if n < 1:
          return False
        elif n == 1:
            return True
        else:
            while n%2==0:
                n = n / 2

            if n == 1:
                return True
            else:
                return False

        