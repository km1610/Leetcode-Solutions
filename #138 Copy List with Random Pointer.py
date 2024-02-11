"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        p = head
        while p!=None:
            new_node = Node(p.val)
            hashmap[p] = new_node
            p=p.next
        hashmap[None]=None

        p = head
        new_head = q = hashmap[head]
        while p!=None:
            q.next = hashmap[p.next]
            q.random = hashmap[p.random]
            q=q.next
            p=p.next
        return new_head
