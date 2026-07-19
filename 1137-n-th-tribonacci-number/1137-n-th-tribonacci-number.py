class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 :
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            f_term = 0
            s_term = 1
            t_term = 1
            for i in range(1,n+1):
                fourth_term = f_term + s_term + t_term
                f_term = s_term
                s_term = t_term 
                t_term = fourth_term
            return f_term 
        