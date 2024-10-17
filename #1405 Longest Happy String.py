from heapq import *
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        limit = [[a,'a'],[b,'b'],[c,'c']]
        limit.sort(reverse=True)
        happy = ""
        while limit[0][0] and limit[1][0] and limit[2][0]:
            happy += limit[0][1] + limit[1][1] + limit[2][1]
            limit[0][0]-=1
            limit[1][0]-=1
            limit[2][0]-=1

        while limit[0][0] and limit[1][0]:
            happy += limit[0][1] + limit[1][1]
            limit[0][0]-=1
            limit[1][0]-=1
        
        if limit[0][0] == 0:
            return happy

        idx = []
        for i in range(len(happy)):
            if happy[i:i+2]==limit[0][1] + limit[1][1]:
                idx.append(i)

        p=0
        for index in idx:
            i = index+p
            if not limit[0][0]:
                break
            happy = happy[:i] + limit[0][1] + limit[0][1] + happy[i+1::]
            limit[0][0]-=1
            i+=2
            p+=1

        if limit[0][0]==0:
            return happy

        for i in range(len(happy)-1):
            if not limit[0][0]:
                break
            if happy[i:i+2] == limit[1][1] + limit[2][1]:
                if limit[0][0]>1:
                    happy = happy[:i+1] + limit[0][1] + limit[0][1] + happy[i+1::]
                    limit[0][0]-=2
                else:
                    happy = happy[:i+1] + limit[0][1] + happy[i+1::]
                    limit[0][0]-=1
        if limit[0][0]>=2:
            happy += limit[0][1] + limit[0][1]
        elif limit[0][0]>=1:
            happy += limit[0][1]

        return happy            
