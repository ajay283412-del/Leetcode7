class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        s=0
        for i in nums:
            s=s+i
            result.append(s)
        return result        
