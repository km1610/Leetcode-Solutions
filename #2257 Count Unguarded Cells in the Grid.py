class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[True for i in range(n)] for j in range(m)]
        occupied = set()
        
        for i in walls:
            grid[i[0]][i[1]] = False
            occupied.add((i[0],i[1]))

        for i in guards:
            grid[i[0]][i[1]] = False
            occupied.add((i[0],i[1]))
        
        for i in guards:
            row, col = i[0], i[1]

            # going north
            r = row-1
            while r>=0 and grid[r][col]:
                occupied.add((r,col))
                r -= 1
            
            # going south
            r = row+1
            while r<m and grid[r][col]:
                occupied.add((r,col))
                r += 1

            # going west
            c = col-1
            while c>=0 and grid[row][c]:
                occupied.add((row,c))
                c -= 1
            
            # going east
            c = col+1
            while c<n and grid[row][c]:
                occupied.add((row,c))
                c += 1
        
        return (m*n) - len(occupied)
