class Solution:
    def totalMoney(self, n: int) -> int:
        money=0
        count=1
        for i in range(n):
            if i%7==0:
                count=i//7+1
            else:
                count+=1
            money+=count
        return money
