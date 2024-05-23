class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        def find(i, subset, subs):
            if i==len(nums):
                if subset:
                    subs.append(subset)
                return subs
            subs = find(i+1,subset,subs)
            if subset:
                a = subset.copy()
                a.append(nums[i])
                flag = False
                for j in subset:
                    if nums[i]-j==k:
                        flag = True
                if not flag:
                    subs = find(i+1,a,subs)
            else:
                a = subset.copy()
                a.append(nums[i])
                subs = find(i+1,a,subs)

            return subs
        return len(find(0,[],[]))
