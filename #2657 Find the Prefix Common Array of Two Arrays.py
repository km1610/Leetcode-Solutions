class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        f1, f2 = {}, {}
        s1,s2 = set(), set()

        n = len(A)

        C=[]

        for i in range(n):
            s1.add(A[i])
            s2.add(B[i])

            if A[i] in f1:
                f1[A[i]]+=1
            else:
                f1[A[i]]=1

            if B[i] in f2:
                f2[B[i]]+=1
            else:
                f2[B[i]]=1

            s = s1.intersection(s2)

            c = 0

            for j in s:
                c+=(f1[j]+f2[j])//2

            C.append(c)
        
        return C
