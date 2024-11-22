class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])

        patterns = []

        for i in range(m):
            s = ''
            pattern = {matrix[i][0]:'o',abs(matrix[i][0]-1):'t'}
            for j in range(n):
                s += pattern[matrix[i][j]]
            patterns.append(s)
            
        unique = set(patterns)
        groups = defaultdict(int)
        for i in unique:
            for j in range(m):
                if patterns[j] == i:
                    groups[i] += 1

        return max(groups.values())
