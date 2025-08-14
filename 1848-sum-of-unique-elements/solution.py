from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        ans = 0
        for k, v in d.items():
            if v == 1:
                ans += k
        
        return ans
       
                  
        
