def get_freq(letters):
    freq = {}
    for i in letters:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

def calc_score(string,scores):
    score = 0
    for i in string:
        score = score + scores[ord(i)-97]
    return score

def cond(string,freq):
    a = freq.copy()
    for i in string:
        if i not in a:
            return False
        a[i]-=1
        if a[i]==-1:
            return False
    return True

def form_string(i,words,freq,scores,string):
    if i==len(words):
        if cond(string,freq):
            return calc_score(string,scores)
        return 0
    return max(form_string(i+1,words,freq,scores,string+words[i]),form_string(i+1,words,freq,scores,string))
    

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = get_freq(letters)
        return form_string(0,words,freq,score, "")
