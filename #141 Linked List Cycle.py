# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hash = {}

        p=head
        i=0

        while p!=None:
            if p not in hash:
                hash[p] = i
                i+=1
                p=p.next
            else:
                return True
        return False
