class Solution:
    def reverseWords(self, s: str) -> str:
        str_to_list = s.split()
        str_to_list = str_to_list[::-1]
        ans = " ".join(str_to_list)
        return ans
        
        

        