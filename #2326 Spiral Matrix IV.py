# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range (n)] for j in range(m)]

        p = head
        row, col = 0,0
        i,j = 0,0
        while p:
            while p and j<n-col:
                matrix[i][j] = p.val
                j+=1
                p=p.next
            j -= 1
            i += 1
            # print(matrix)
            while p and i<m-row:
                matrix[i][j] = p.val
                i+=1
                p=p.next
            i -= 1
            j -= 1
            # print(matrix)
            while p and j>=0+col:
                matrix[i][j] = p.val
                j-=1
                p=p.next
            i-=1
            j+=1
            # print(matrix)
            while p and i>=0+row+1:
                matrix[i][j] = p.val
                i-=1
                p=p.next
            # print(matrix)

            row += 1
            col += 1

            i = row
            j = col
        return matrix
