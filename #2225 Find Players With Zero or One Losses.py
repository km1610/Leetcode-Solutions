class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        for i in matches:
            if i[0] in d.keys():
                d[i[0]][0]+=1
            else:
                d[i[0]] = [1,0]
            
            if i[1] in d.keys():
                d[i[1]][1]+=1
            else:
                d[i[1]] = [0,1]

        answers = [[],[]]
        for i in d.keys():
            if d[i][1]==0:
                answers[0].append(i)
            if d[i][1]==1:
                answers[1].append(i)
        answers[0].sort()
        answers[1].sort()
        return answers
