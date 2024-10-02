class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))
        rank = []
        ranks = {}
        for i in range(len(a)):
            ranks[a[i]] = i + 1
        for i in arr:
            rank.append(ranks[i])
        return rank
