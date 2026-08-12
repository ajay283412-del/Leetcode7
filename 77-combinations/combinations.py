class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(start):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for num in range(start, n + 1):
                sol.append(num)
                backtrack(num + 1)
                sol.pop()

        backtrack(1)
        return res
        