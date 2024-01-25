class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)

        # Recursive method
        # if m==0 or n==0:
        #     return 0
        # if text1[m-1]==text2[n-1]:
        #     return 1 + self.longestCommonSubsequence(text1[:m-1],text2[:n-1])
        # return max(self.longestCommonSubsequence(text1[:m-1],text2),self.longestCommonSubsequence(text1,text2[:n-1]))

        matrix =  []
        
        for i in range(m+1):
            l = []
            for j in range(n+1):
                l.append(0)
            matrix.append(l)
        i=j=1
        while i<=m and j<=n:
            if text1[i-1]==text2[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

            if j==n and i<=m:
                i+=1
                j=1
            else:
                j+=1
        return matrix[m][n]
