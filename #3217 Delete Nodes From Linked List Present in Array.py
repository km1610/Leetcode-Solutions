# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        p = head
        while p.val in nums:
            p=p.next
        head = p
        if head==None:
            return head
        q=head
        while q.next!=None:
            if q.next.val in nums:
                t = q.next.next
                q.next = t
            else:
                q = q.next
        return head
