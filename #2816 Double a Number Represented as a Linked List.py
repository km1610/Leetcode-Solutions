# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    prev = None
    while head!=None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = reverse(head)
        p = q = head
        c = 0
        while p!=None:
            val = p.val*2 + c
            p.val = val%10
            c = val//10
            q = p
            p=p.next
        if c!=0:
            new = ListNode(c)
            q.next = new
        head = reverse(head)
        return head
        
