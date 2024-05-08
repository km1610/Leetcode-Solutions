class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = 1
        out = []
        ranks = {}
        scores = sorted(score)
        scores.reverse()
        for i in scores:
            ranks[i] = rank
            rank+=1
        rank = 1
        for i in score:
            if ranks[i]==1:
                out.append("Gold Medal")
            elif ranks[i]==2:
                out.append("Silver Medal")
            elif ranks[i]==3:
                out.append("Bronze Medal")
            else:
                out.append(str(ranks[i]))
            rank+=1
        return out
