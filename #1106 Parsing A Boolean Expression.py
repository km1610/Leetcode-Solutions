class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in expression:
            if i!=")" and i!=",":
                if i == "t":
                    stack.append(1)
                elif i == "f":
                    stack.append(0)
                else:
                    stack.append(i)
            if i == ")":
                subexp = []
                while stack and stack[-1]!="(":
                    subexp.append(stack.pop())
                stack.pop()
                if stack[-1]:
                    op = stack.pop()
                    e = subexp[0]
                    if op == "&":
                        for x in subexp:
                            e = e&x
                    if op == "|":
                        for x in subexp:
                            e = e|x
                    if op == "!":
                        e = not e
                    stack.append(e)
        return stack[-1] == 1
                 
