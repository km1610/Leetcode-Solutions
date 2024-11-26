class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = {}
        for i in range(n):
            indegree[i] = 0
        for i in edges:
            a,b = i[0], i[1]
            indegree[b] += 1
        champion_num = 0
        champion = -1
        for i in indegree:
            if indegree[i] == 0:
                champion_num+=1
                champion = i
        if champion_num == 1:
            return champion
        return -1
