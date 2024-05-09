class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness_sum = 0
        happiness.sort()
        i = 0
        while k:
            score=happiness.pop()-i
            if score<0:
                score=0
            happiness_sum+=score
            i+=1
            k-=1
        return happiness_sum
