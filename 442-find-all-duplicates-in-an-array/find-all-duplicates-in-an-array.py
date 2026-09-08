class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        d=set()
        for i in nums:
            if i in d:
                l.append(i)
            else:
                d.add(i)
        return l