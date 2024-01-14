class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n,m = len(word1),len(word2)
        if m!=n:
            return False
        freq1,freq2 = {},{}

        for i in range(n):
            if word1[i] in freq1:
                freq1[word1[i]] += 1
            else:
                freq1[word1[i]] = 1

            if word2[i] in freq2:
                freq2[word2[i]] += 1
            else:
                freq2[word2[i]] = 1
        l1,l2 = [],[]

        for i in freq1:
            if i in freq2:
                l1.append(freq1[i])
            else:
                return False

        for i in freq2:
            if i in freq1:
                l2.append(freq2[i])
            else:
                return False

        l1.sort()
        l2.sort()

        if l1==l2:
            return True
        return False
