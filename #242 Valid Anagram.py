class Solution(object):
    def isAnagram(self, s, t):
        h_s = {}
        h_t = {}

        if len(s)!=len(t):
            return False
            
        for i in s:
            if i in h_s:
                h_s[i]+=1
            else:
                h_s[i] = 1
        for i in t:
            if i in h_t:
                h_t[i]+=1
            else:
                h_t[i] = 1 
        
        for i in h_s:
            if i not in h_t or h_t[i]!=h_s[i]:
                return False
        return True
