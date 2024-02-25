class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)

        if n>m:
            return False

        freq = {}
        count = {}
        counter = 0

        for i in range(n):
            if s1[i] in freq:
                freq[s1[i]]+=1
            else:
                freq[s1[i]] = 1
        
        for i in range(n):
            if s2[i] in freq:
                if s2[i] in count:
                    count[s2[i]] += 1
                else:
                    count[s2[i]] = 1
            
                if freq[s2[i]]>=count[s2[i]]:
                    counter+=1

        if counter==n:
            return True

        for i in range(1,m-n+1):
        
            if s2[i-1] in count:
                if freq[s2[i-1]]>=count[s2[i-1]]:
                    counter-=1

                if count[s2[i-1]]>0:
                    count[s2[i-1]]-=1

            if s2[i+n-1] in freq:
                if s2[i+n-1] in count:
                    count[s2[i+n-1]] += 1
                else:
                    count[s2[i+n-1]] = 1
            
                if freq[s2[i+n-1]]>=count[s2[i+n-1]]:
                    counter+=1

            if counter==n:
                return True
        
        return False

        

        
                
