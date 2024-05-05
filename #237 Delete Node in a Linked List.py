# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        p=node
        if p.next==None:
            node = None
        else:
            while p.next!=None:
                p.val=p.next.val
                p=p.next
            p=node
            while p.next.next!=None:
                p=p.next
            p.next=None
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
