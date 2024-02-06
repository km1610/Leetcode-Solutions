class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A','E','I','O','U','a','e','i','o','u'}

        l = list(s)
        non_con = []

        for i in l:
            if i in vowels:
                non_con.append(i)
        
        non_con.sort()

        j=0
        for i in range(len(l)):
            if l[i] in vowels:
                l[i] = non_con[j]
                j+=1
        
        return ''.join(l)
