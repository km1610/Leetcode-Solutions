class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        i=0
        newInts = []

        start = intervals[i][0]
        end = intervals[i][1]

        while i<len(intervals)-1:            
            if end>=intervals[i+1][0]:
                if end<intervals[i+1][1]:
                    end = intervals[i+1][1]
            else:
                newInts.append([start,end])
                start = intervals[i+1][0]
                end = intervals[i+1][1]
            i+=1
        newInts.append([start,end])
        return newInts
      
