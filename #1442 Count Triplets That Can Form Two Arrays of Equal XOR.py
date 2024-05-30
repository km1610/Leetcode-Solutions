class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        c = 0
        for i in range(0,n-1):
            a = 0
            for j in range(i+1,n):
                b = 0
                a = a^arr[j-1]
                for k in range(j,n):
                    b = b^arr[k]
                    if b==a:
                        c+=1                    
        return c        
