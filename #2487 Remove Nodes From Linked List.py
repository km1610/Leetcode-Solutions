# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        items = []
        p = head
        while p!=None:
            items.append(p.val)
            p=p.next
        stack = []
        i = -1
        m = -float('inf')
        while i>=-len(items):
            if items[i]>=m:
                stack.append(items[i])
                m = items[i]
            i-=1
        p = head
        i = -1
        while i>=-len(stack):
            p.val = stack[i]
            q=p
            i-=1
            p=p.next
        q.next = None
        return head
