class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        rows = len(matrix)
        cols = len(matrix[0])
        i=j=0
        start_row=start_col=0

        #keep count of elements
        total = rows*cols
        count = 0

      
        while count<total and i<len(matrix) and j<len(matrix[0]):
            i=start_row
            j=start_col
          
            while j<cols: #going right
                res.append(matrix[i][j])
                # print(i,j)
                j+=1
                count+=1
            start_row+=1
            j-=1
            i+=1
          
            if count<total:
                while i<rows: #going down
                    res.append(matrix[i][j])
                    # print(i,j)
                    i+=1
                    count+=1
                cols-=1
                j-=1
                i-=1
              
            if count<total:
                while j>=start_col: #going left
                    res.append(matrix[i][j])
                    # print(i,j)
                    j-=1
                    count+=1
                rows-=1
                j+=1
                i-=1
              
            if count<total:  
                while i>=start_row: #going up
                    res.append(matrix[i][j])
                    # print(i,j)
                    i-=1
                    count+=1
                start_col+=1
                i+=1

        return res
