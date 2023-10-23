class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        pivot = strs[0]
        common=''
        for i in range(len(pivot)):
            for j in strs[1::]:
                if pivot[i]!=j[i]:
                    return common
            common+=pivot[i]
        return common
