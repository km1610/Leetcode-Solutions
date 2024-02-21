# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p,q,b = head,head,head
        i,n = 0,1
        while p!=None:
            p=p.next
            n+=1
        p=head

        while i!=(n//2)-1:
            while q.next!=None:
                b=q
                q=q.next
            t = p.next
            p.next = q
            q.next = t
            b.next=None
            p=p.next.next
            q=p
            b=p
            i+=1        

        return head
