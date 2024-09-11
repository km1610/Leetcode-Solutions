class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        final = []
        
        for i in path:
            if i == "." or i=="":
                continue
            elif i == "..":
                if final:
                    final.pop()
            else:
                final.append(i)

        final = "/" + "/".join(final)

        return final
