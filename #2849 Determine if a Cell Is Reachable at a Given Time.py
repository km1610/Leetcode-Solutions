class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        t_taken = 0
        if abs(sx-fx)==0 and abs(sy-fy)==0 and t==1:
            return False
        if abs(sx-fx)==0 and abs(sy-fy)==0:
            return True
        elif abs(sx-fx)==0:
            t_taken+= abs(sy-fy)
        elif abs(sy-fy)==0:
            t_taken+= abs(sx-fx)
        else:
            if abs(sx-fx)<abs(sy-fy):
                if sy>fy:
                    fy+=abs(sx-fx)
                else:
                    sy+=abs(sx-fx)
            else:
                if sx>fx:
                    fx+=abs(sy-fy)
                else:
                    sx+=abs(sy-fy)

            t_taken+=abs(sx-fx) + abs(sy-fy)

        if t_taken<=t:
            return True
        return False
