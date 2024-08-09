class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        # since it's a 3x3 (constant) magic sqaure -> sum of all rows and columns will be 15 (constant)

        if row<3 or col<3:
            return 0

        count = 0
        
        def check_square(i,j):
            row_sum = [0,0,0]
            col_sum = [0,0,0]
            diag_sum = [0,0]
            used = set()

            for x in range(3):
                for y in range(3):
                    if grid[x+i][y+j] in used:
                        return False
                    if grid[x+i][y+j]<1 or grid[x+i][y+j]>9:
                        return False
                    used.add(grid[x+i][y+j])

            for x in range(3):
                s = 0
                for y in range(3):
                    s += grid[x+i][j+y]
                row_sum[x] = s

            for x in range(3):
                s = 0
                for y in range(3):
                    s += grid[y+i][j+x]
                col_sum[x] = s

            for x in range(3):
                diag_sum[0] += grid[i+x][j+x]
                diag_sum[1] += grid[i+2-x][j+2-x]
                
            if col_sum[0]==col_sum[1]==col_sum[2]==row_sum[0]==row_sum[1]==row_sum[2]==diag_sum[0]==diag_sum[1]==15:
                return True
            return False
        
        for i in range(row-2): # row - 3 + 1
            for j in range(col-2): # col - 3 + 1
                if check_square(i,j):
                    count+=1

        return count
