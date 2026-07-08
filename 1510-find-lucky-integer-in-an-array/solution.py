class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=-1
        for k,v in d.items():
            if k==v:
                ans=max(ans,v)
        return ans
