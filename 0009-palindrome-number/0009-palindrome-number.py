class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        return False    
        #  temp = x
        #  reverseNum = 0
        #  while x > 0:
        #     lastdigit = x % 10
        #     reverseNum =  (reverseNum * 10 ) + lastdigit
        #     x = x // 10
        #  if reverseNum == temp:
        #     return True
        #  else:
        #     return False       
        