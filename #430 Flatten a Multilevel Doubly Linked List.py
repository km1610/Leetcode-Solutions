"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        p = head

        while p!=None:
            if p.child!=None:

                temp_next = p.next

                q = p.child

                q.prev = p

                p.next = p.child

                p.child=None

                while q.next!=None:
                    q=q.next

                q.next = temp_next
                if temp_next!=None:
                    temp_next.prev = q

            p=p.next
        return head
