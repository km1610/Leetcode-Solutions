class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)

        freq = {}

        max_len = 0
        max_odd = 0

        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for i in freq:
            if freq[i]%2==0:
                max_len+=freq[i]
            else:
                if freq[i]<=max_odd:
                    max_len+=freq[i]-1
                else:
                    if max_odd!=0:
                        max_len+=max_odd-1
                    max_odd = freq[i]
                    

        max_len+=max_odd
    
        return max_len
        
