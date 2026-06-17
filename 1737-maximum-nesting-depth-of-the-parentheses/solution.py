class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxcount=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
                count+=1
            elif i==")":
                if count>maxcount:
                    maxcount=count
                count-=1
                stack.pop()
        return maxcount
        
