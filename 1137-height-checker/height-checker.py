class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        expected=sorted(heights)
        a=0
        for i in range(n):
            if heights[i] !=expected[i]:
                a +=1
        return a