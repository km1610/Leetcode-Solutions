class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def func(curr_sum,i,comb):
            if curr_sum == target:
                if comb not in out:
                    out.append(comb)
                return
            if curr_sum>target or i == len(candidates):
                return
            func(curr_sum, i+1, comb)
            func(curr_sum + candidates[i],i+1,comb + [candidates[i]])
            func(curr_sum + candidates[i],i,comb + [candidates[i]])
        func(0,0,[])
        return out
