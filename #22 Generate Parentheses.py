class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen(open,close,string):
            if len(string)==n*2:
                res.append(string)
            else:
                if open==n:
                    gen(open,close+1,string+")")
                else:
                    if close<open:
                        gen(open,close+1,string+")")
                    gen(open+1,close,string+"(")
        gen(0,0,"")
        return res
