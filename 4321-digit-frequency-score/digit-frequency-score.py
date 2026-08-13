class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        t=0
        for digit in str(n):
            t+=int(digit)
        return t