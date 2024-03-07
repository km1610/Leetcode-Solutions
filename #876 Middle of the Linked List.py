# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        p = head
        while p!=None:
            n+=1
            p=p.next
        
        mid = (n//2)+1

        p = head
        i = 0

        while p!=None and i+1!=mid:
            p=p.next
            i+=1
        
        return p

        
