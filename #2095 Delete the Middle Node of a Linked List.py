# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        N = 0
        p = head
        while p:
            N += 1
            p = p.next
        if N==1:
            return None
        mid = (N//2)
        p = q = head
        while mid and p:
            q = p
            p = p.next
            mid-=1
        if p:
            q.next = p.next
        return head
