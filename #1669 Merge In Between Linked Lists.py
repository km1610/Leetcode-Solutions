# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        n = 1
        p = list1
        while n<a:
            p=p.next
            n+=1
        a_node = p

        n=0
        p = list1
        while n!=b:
            p=p.next
            n+=1
        b_node = p.next

        q = list2

        while q.next!=None:
            q=q.next
        
        a_node.next = list2
        q.next = b_node

        return list1
