class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newint = []
        intervals.sort()
        n = len(intervals)
        i = 0
        
        while i < n:
            if i==0:
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                if intervals[i][0]<=end:
                    end = max(intervals[i][1],end)
                if intervals[i][0]>end:
                    newint.append([start,end])
                    start = intervals[i][0]
                    end = intervals[i][1]
            i+=1
        newint.append([start,end])
        return newint
