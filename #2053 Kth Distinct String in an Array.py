class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        strings = {}
        for i in arr:
            if i in strings:
                strings[i]+=1
            else:
                strings[i]=1
        for i in strings:
            if strings[i]==1:
                k-=1
                if not k:
                    return i
        return ""
