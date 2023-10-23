class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        order = [0]*(n*n)

        rows = n
        cols = n

        start_row=start_col=0
        total = rows*cols
        count = 0
        i=j=0
        while count<total and i<n and j<n:
            i=start_row
            j=start_col
            while j<cols:
                count+=1
                order[(i*n)+j] = count
                j+=1    
            start_row+=1
            j-=1
            i+=1
            if count<total:
                while i<rows:
                    count+=1
                    order[(i*n)+j] = count
                    i+=1
                cols-=1
                j-=1
                i-=1
            if count<total:
                while j>=start_col:
                    count+=1
                    order[(i*n)+j] = count
                    j-=1
                rows-=1
                j+=1
                i-=1
            if count<total:  
                while i>=start_row:
                    count+=1
                    order[(i*n)+j] = count
                    i-=1
                start_col+=1
                i+=1

        matrix = []

        print(order)
        for i in range(0,n*n,n):
            sub = []
            for j in range(n):
                sub.append(order[i+j])
            matrix.append(sub)
        return matrix
        

