class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        for i in range(len(arr1)):
            arr1[i] = str(arr1[i])
        for i in range(len(arr2)):
            arr2[i] = str(arr2[i])
        arr1.sort()
        arr2.sort()
        i,j = 0,0
        l = 0
        while i < len(arr1):
            if j==len(arr2):
                break
            k = 0
            while k<min(len(arr1[i]),len(arr2[j])) and arr1[i][k] == arr2[j][k]:
                k+=1
            l = max(l,k)

            if arr1[i]<arr2[j]:
                i += 1
            else:
                j += 1

        return l
