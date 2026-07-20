class Solution:
    def average(self, salary: List[int]) -> float:
        ans = 0
        count = 0
        salary.sort()
        for i in range(1,len(salary)-1):
            ans += salary[i]
            count += 1
        return ans / count        