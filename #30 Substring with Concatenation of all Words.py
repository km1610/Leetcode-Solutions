class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        m = len(words[0])
        word_length = m*n
        output = []
        global_hash = {}

        for i in words:
            if i in global_hash:
                global_hash[i]+=1
            else:
                global_hash[i]=1

        def check_concat(string):
            hash = {}
            for i in range(0,len(string),m):
                if string[i:i+m] in global_hash:
                    if string[i:i+m] not in hash:
                        hash[string[i:i+m]] = 1
                    elif hash[string[i:i+m]]<global_hash[string[i:i+m]]:
                        hash[string[i:i+m]] += 1
                    else:
                        return False
                else:
                    return False
            return True


        for i in range(len(s)-word_length+1):
            if check_concat(s[i:i+word_length])==True:
                output.append(i)
        return output
        
