class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        po=[]
        ne=[]
        a=[]
        for i in nums:
            if i<0:
                ne.append(i)
            else:
                po.append(i)
        if len(ne)==len(po):
            for i in range(len(ne)):
                a.append(po[i])
                a.append(ne[i])
        elif len(ne)<len(po):
            for i in range(len(ne)):
                a.append(po[0])
                po.pop(0)
                a.append(ne[i])
            a.extend(po)
        else:
            for i in range(len(po)):
                a.append(po[i])
                a.append(ne[0])
                ne.pop(0)
            a.extend(ne)
        return a
