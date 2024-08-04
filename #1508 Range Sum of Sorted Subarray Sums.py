class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_array = []
        mod = (10**9)+7
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                sum_array.append(s)
        sum_array.sort()
        return sum(sum_array[left-1:right])%mod
