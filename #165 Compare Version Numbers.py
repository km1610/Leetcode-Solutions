class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1,v2 = version1.split('.'),version2.split('.')
        n,m = len(v1),len(v2)
        i=0

        if m>n:
            v1.extend(['0']*(m-n))
        if n>m:
            v2.extend(['0']*(n-m))

        while i<max(m,n) and int(v1[i])==int(v2[i]):
            i+=1

        if i==max(m,n):
            return 0
        if int(v1[i])>int(v2[i]):
            return 1
        if int(v1[i])<int(v2[i]):
            return -1
        return 0
