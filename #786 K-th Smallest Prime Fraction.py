class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = {}
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                fractions[arr[i]/arr[j]] = [arr[i],arr[j]]
        values = sorted(fractions.keys())
        return fractions[values[k-1]]
