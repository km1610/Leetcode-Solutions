# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N=0
        p=head
        while p!=None:
            N=N+1
            p=p.next
        if N==1 and n==1:
            head=None
        elif n==1:
            p=q=head
            while p.next!=None:
                q=p
                p=p.next
            q.next=None
        elif n==N:
            head=head.next
        else:
            k=N-n+1
            N=1
            p=q=head
            while p!=None and N!=k:
                q=p
                p=p.next
                N+=1
            q.next=p.next
        return head
