class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=0
        m=len(accounts)
        for i in accounts:
            rsum=sum(i)
            if rsum>maxsum:
                maxsum=rsum
        return maxsum

        
