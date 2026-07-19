class Solution:
    def fib(self, n: int) -> int:
        if n == 0 :
            return 0 
        elif n == 1:
            return 1
        else:
            first_term = 0
            second_term = 1
            for i in range(1,n+1):
                third_term = first_term + second_term

                first_term = second_term
                second_term = third_term
            return first_term


        