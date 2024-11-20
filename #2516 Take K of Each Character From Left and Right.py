class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s.count('a')<k or s.count('b')<k or s.count('c')<k:
            return -1
        if k==0:
            return 0
        
        l, r = 0,0
        n = len(s)
        freq = {'a':0,'b':0,'c':0}
        window_freq = {'a':0,'b':0,'c':0}

        for i in s:
            freq[i]+=1

        max_valid_window = 0

        while r<n:
            while r<n and freq['a']-window_freq['a']>=k and freq['b']-window_freq['b']>=k and freq['c']-window_freq['c']>=k:
                window_freq[s[r]] += 1
                r += 1

            max_valid_window = max(max_valid_window, r-l-1)

            while l<r and (freq['a']-window_freq['a']<k or freq['b']-window_freq['b']<k or freq['c']-window_freq['c']<k):
                window_freq[s[l]] -= 1
                l+=1

            max_valid_window = max(max_valid_window, r-l)            
        
        return n-max_valid_window
