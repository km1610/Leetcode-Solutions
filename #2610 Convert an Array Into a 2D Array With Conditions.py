class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = [[]]
        d={}
        for i in nums:
            d[i] = 0
            
        for i in nums:
            if len(matrix)<=d[i]:
                matrix.append([])
            matrix[d[i]].append(i)
            d[i] += 1
        
        ans = []
        for i in matrix:
            if len(i)!=0:
                ans.append(i)
        
        return ans
