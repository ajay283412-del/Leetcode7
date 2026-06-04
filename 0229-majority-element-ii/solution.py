class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        freq=dict()
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        t=n//3
        for (k,v) in freq.items():
                if v>t:
                    res.append(k)
        return res
