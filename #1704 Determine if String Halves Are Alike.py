class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:(n//2)]
        b = s[(n//2):]

        n_a = n_b = 0

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(n//2):
            if a[i] in vowels:
                n_a+=1
            if b[i] in vowels:
                n_b+=1
        
        if n_a==n_b:
            return True
        return False
