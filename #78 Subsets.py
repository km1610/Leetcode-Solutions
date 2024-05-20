class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def find(i,subset,subs):
            if i==len(nums):
                subs.append(subset)
                return subs
            a,b = subset.copy(), subset.copy()
            b.append(nums[i])
            subs = find(i+1,a,subs)
            subs = find(i+1,b,subs)
            return subs
        return find(0,[],[])
