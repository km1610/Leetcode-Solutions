class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        hashmap = {}
        for i in chars:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        def good(s):
            temp = hashmap.copy()
            flag = 1
            for i in s:
                if i not in temp:
                    flag=0
                    break
                else:
                    if temp[i]==0:
                        flag=0
                        break
                    else:
                        temp[i]-=1
                                    
            return flag
        
        ans = 0

        for i in words:
            if good(i):
                ans+=len(i)

        return ans        
