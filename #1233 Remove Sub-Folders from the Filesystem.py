class TrieNode:
    def __init__(self, val = ""):
        self.val = val
        self.children = {}
        self.endOfFile = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for i in range(len(folder)):
            folder[i] = folder[i].split("/")[1::]

        Trie = TrieNode()
        for i in folder:
            curr = Trie
            j = 0
            while j<len(i) and i[j] in curr.children:
                curr = curr.children[i[j]]
                j+=1
            while j!=len(i):
                curr.children[i[j]] = TrieNode(i[j])
                curr = curr.children[i[j]]
                j+=1
            curr.endOfFile = True

        output = []
        def Traverse(curr,string):
            for i in curr.children:
                new_string = string + "/" + i
                if curr.children[i].endOfFile:
                    output.append(new_string)
                    new_string = string
                else:
                    Traverse(curr.children[i], new_string)
                    
        Traverse(Trie,"")
        return output
