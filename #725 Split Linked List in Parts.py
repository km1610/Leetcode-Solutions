# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N = 0
        p = head
        while p:
            N += 1
            p=p.next
        split_n = []
        if k>=N:
            split_n.extend([1]*N)
            split_n.extend([0]*(k-N))
        else:
            r = N%k
            q = N//k
            while k:
                if r:
                    split_n.append(q+1)
                    r-=1
                else:
                    split_n.append(q)
                k-=1
        i = 0
        p = q = head
        split = []
        while i<len(split_n):
            q = p
            n = split_n[i]
            split.append(p)
            while n:
                q = p
                p=p.next
                n-=1
            if q:
                q.next = None
            i += 1
        return split
