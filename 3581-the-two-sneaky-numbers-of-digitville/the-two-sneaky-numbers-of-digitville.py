class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d=dict()
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        res=[]
        for (k,v)in d.items():
            if v==2:
                res.append(k)
        return res