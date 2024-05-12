# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head!=None and head.val ==  val:
            temp = head.next
            head.next = None
            head = temp
        p = q = head
        while p!=None:
            if p!=None and p.val == val:
                temp = p.next
                q.next = temp
                p = temp
            else:
                q = p
                p = p.next
        return head
