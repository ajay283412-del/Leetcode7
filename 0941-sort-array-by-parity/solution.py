class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenlist=[]
        oddlist=[]
        for i in nums:
            if i%2==0:
                evenlist.append(i)
            else:
                oddlist.append(i)
        return evenlist+oddlist
