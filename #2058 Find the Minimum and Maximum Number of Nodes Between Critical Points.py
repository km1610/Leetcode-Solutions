# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        dist = []
        if head.next and head.next.next:
            p = head
            q = head.next
            r = head.next.next
            N = 0
            while r:
                N += 1
                if q.val > p.val and q.val > r.val:
                    critical_points.append(N)
                if q.val < p.val and q.val < r.val:
                    critical_points.append(N)
                p = p.next
                q = q.next
                r = r.next
            if critical_points:
                for i in range(len(critical_points)-1):
                    dist.append(critical_points[i+1]-critical_points[i])
                if dist:
                    return [min(dist), critical_points[-1]-critical_points[0]]
        return [-1,-1]
        
