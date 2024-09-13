class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]*(len(arr)+1)
        xor = 0
        for i in range(len(arr)):
            xor = xor ^ arr[i]
            xors[i+1] = xor

        res = []
        for i in queries:
            l,r = i[0],i[1]
            res.append(xors[r+1]^xors[l])
        return res
