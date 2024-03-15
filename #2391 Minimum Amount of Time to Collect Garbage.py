class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        metal,plastic,glass = {0:0},{0:0},{0:0}

        for i in range(len(garbage)):
            m = garbage[i].count('M')
            if m>0:
                metal[i] = m
            p = garbage[i].count('P')
            if p>0:
                plastic[i] = p
            g = garbage[i].count('G')
            if g>0:
                glass[i] = g

        travel.insert(0,0)

        t = 0

        for i in metal:
            t += metal[i]

        for i in plastic:
            t += plastic[i]

        for i in glass:
            t += glass[i]

        max_m,max_p,max_g = max(metal),max(plastic),max(glass)


        t += sum(travel[:max_m+1]) + sum(travel[:max_p+1]) + sum(travel[:max_g+1])

        return t
