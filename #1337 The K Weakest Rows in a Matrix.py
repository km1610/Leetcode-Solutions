class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        for i in range(len(mat)):
            soldiers.append([mat[i].count(1),i])
        soldiers.sort()
        weak = []
        for i in range(k):
            weak.append(soldiers[i][1])
        return weak
