# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
        else:
            p,q = list1,list2
            head = ListNode(-1)
            r = head
            while p!=None and q!=None:
                if p.val<q.val:
                    new = ListNode(p.val)
                    r.next = new
                    p=p.next
                else:
                    new = ListNode(q.val)
                    r.next = new
                    q=q.next
                r=r.next
            while p!=None:
                new = ListNode(p.val)
                r.next = new
                r=r.next
                p=p.next
            while q!=None:
                new = ListNode(q.val)
                r.next = new
                r=r.next
                q=q.next
            head = head.next
            return head
