def merge_intervals(intervals):
    intervals.sort()
    ans = []
    i=0

    while i < len(intervals)-1:
        if intervals[i][1]<intervals[i+1][0]:
            ans.append(intervals[i])
        else:
            intervals[i+1][0] = intervals[i][0]
            intervals[i+1][1] = max(intervals[i][1],intervals[i+1][1])
        i+=1
    ans.append(intervals[i])
  
    return ans

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {}
        first_ind = {}
        for i in range(len(s)):
            last_ind[s[i]] = i
            if s[i] not in first_ind:
                first_ind[s[i]] = i
        intervals = []
        for i in last_ind:
            intervals.append([first_ind[i],last_ind[i]])
          
        intervals = merge_intervals(intervals)
        answer = []
      
        for i in intervals:
            answer.append(i[1]-i[0]+1)
        return answer
