# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
def gcd(x,y):
    return math.gcd(x,y)

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        inp=[]
        while p!=None:
            inp.append(p.val)
            p=p.next
        out=[inp[0]]
        for i in range(len(inp)-1):
            out.append(gcd(inp[i],inp[i+1]))
            out.append(inp[i+1])

        p=head
        i=0
        while p.next!=None:
            p.val = out[i]
            i+=1
            p=p.next
        p.val= out[i]
        i+=1
        while i!=len(out):
            n=ListNode(out[i])
            p.next=n
            p=p.next
            i+=1
        return head
