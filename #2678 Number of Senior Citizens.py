class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for passenger in details:
            if passenger[11:13]>'60':
                c+=1
        return c
