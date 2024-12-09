class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        diff_parity = defaultdict(int)
        for i in range(1, len(nums)):
            if (nums[i] + nums[i-1])%2==0:
                diff_parity[i] += 1
            diff_parity[i] += diff_parity[i-1]
            
        ans = []
        for q in queries:
            f, t = q
            if diff_parity[t] - diff_parity[f] == 0:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
