class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1
        prev = s[0]
        for i in range(1,len(s)):
            if s[i] == prev:
                count += 1
                max_count = max(max_count,count)
            else:
                prev = s[i]
                count = 1
        return max_count
        