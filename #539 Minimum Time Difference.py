class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for i in range(len(timePoints)):
            h,m = map(int,timePoints[i].split(':'))
            minutes.append((h*60)+m)
        minutes.sort()
        timeDiffs = []
        for i in range(len(minutes)):
            timeDiffs.append(min((minutes[(i+1)%len(minutes)]-minutes[i])%1440,(minutes[i]-minutes[(i+1)%len(minutes)])%1440))
        return min(timeDiffs)
