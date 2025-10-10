class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        count=1
        end=intervals[0][1]
        for i in intervals:
            if i[0]>=end:
                end=i[1]
                count+=1
        return n-count
