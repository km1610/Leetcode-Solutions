class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        balloons = []

        i = 0

        n = len(colors)
        set_balloon = []

        while i<n:
            if i==n-1 or colors[i]!=colors[i+1]:
                set_balloon.append(colors[i])
                balloons.append(set_balloon)
                set_balloon = []
            elif colors[i]==colors[i+1]:
                set_balloon.append(colors[i])
            
            i+=1
        # print(balloons)

        d = len(balloons)

        i = j = 0
        time = 0
        while i<d:
            s = len(balloons[i])
            if s!=1:
                sumarr = sum(neededTime[j:j+s])
                maxi = max(neededTime[j:j+s])
                time += sumarr-maxi

            i+=1
            j+=s    

        return time
            
