import math
class Solution:
    def check_dist(self,cx,cy,x,y):
        dist = math.sqrt(((cx-x)**2)+((cy-y)**2))
        return dist
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for i in queries:
            c=0
            for j in points:
                if self.check_dist(i[0],i[1],j[0],j[1])<=i[2]:
                    c+=1
            answer.append(c)
        return answer
