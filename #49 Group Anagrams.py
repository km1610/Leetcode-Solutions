class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        for i in strs:
            str1 = str(sorted(list(i)))
            if not hashmap:
                hashmap[str1] = [i]
            else:
                if str1 in hashmap:
                    hashmap[str1].append(i)
                else:
                    hashmap[str1] = [i]
        for i in hashmap:
            output.append(hashmap[i])
        return output
