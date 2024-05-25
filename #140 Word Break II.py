class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        sentences = []
        n = len(s)

        def form_sentence(used):
            return ' '.join(used)

        def create_breaks(start,used):
            if start==n:
                sentence = form_sentence(used)
                sentences.append(sentence)
            else:
                for i in range(start+1,n+1):
                    if s[start:i] in wordDict:
                        a = used.copy()
                        a.append(s[start:i])
                        create_breaks(i,a)

        create_breaks(0,[])
        return sentences
