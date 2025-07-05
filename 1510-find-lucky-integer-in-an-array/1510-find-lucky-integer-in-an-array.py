class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max((x for x, f in Counter(arr).items() if x==f), default=-1)
        #Constraint is in range
        # freq = [0] * 501
        # for i in arr:
        #     freq[i] += 1
        # for i in range(500,0,-1):
        #     if freq[i] == i:
        #         return i
        # return -1

        # HASHMAP            
        # res = {}
        # for i in range(len(arr)):
        #     if arr[i] not in res:
        #         res[arr[i]] = 1
        #     else:
        #         res[arr[i]] += 1
        # maxi = -1
        # for num,freq in res.items():
        #     if num == freq:
        #         maxi = max(maxi,num)
        # return maxi    
