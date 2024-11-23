class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box),len(box[0])
        for row in range(m):
            curr_obstacle = n
            col = n-1
            while col>=0:
                if box[row][col] == '*':
                    curr_obstacle = col
                elif box[row][col] == '#':
                    box[row][col] = '.'
                    box[row][curr_obstacle-1] = '#'
                    curr_obstacle = curr_obstacle-1
                col -= 1

        newbox = [['.' for row in range(m)] for col in range(n)]
        for row in range(m):
            for col in range(n):
                newbox[col][row] = box[m-row-1][col]
        return newbox
