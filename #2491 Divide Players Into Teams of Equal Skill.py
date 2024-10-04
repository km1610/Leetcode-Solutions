from collections import defaultdict
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)
        chemistry = (s*2)//len(skill)
        exist = {}
        pairs = 0
        sum_of_chemistry = 0
        for i in skill:
            if (chemistry-i) in exist and exist[chemistry-i]:
                exist[chemistry-i] -= 1
                pairs += 1
                sum_of_chemistry += i*(chemistry-i)
            else:
                if i not in exist:
                    exist[i] = 0
                exist[i] += 1
        if pairs!=len(skill)//2:
            return -1
        return sum_of_chemistry
