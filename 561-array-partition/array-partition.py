class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        length=len(nums)
        nums.sort()
        s=0
        for i in range(0,length,2):
            s+=nums[i]
        return s