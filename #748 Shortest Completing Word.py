class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        freq_license = {}

        def compare_freq(f1,word):
            f2 = {}
            for i in word:
                l = i.lower()
                if l>='a'and l<='z':
                    if l in f2:
                        f2[l]+=1
                    else:
                        f2[l]=1
            for i in f1:
                if i not in f2:
                    return False
                f2[i]-=f1[i]
                if f2[i]<0:
                    return False
            return True

        for i in licensePlate:
            l = i.lower()
            if l>='a'and l<='z':
                if l in freq_license:
                    freq_license[l]+=1
                else:
                    freq_license[l]=1
        words.sort(key=len)
        for i in words:
            if compare_freq(freq_license,i):
                return i
