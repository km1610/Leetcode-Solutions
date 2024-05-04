class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0,len(people)-1
        people.sort(reverse=True)
        temp = limit
        boat = 0
        while l<=r:
            temp-=people[l]
            if people[r]<=temp:
                temp-=people[r]
                r-=1
            l+=1
            boat+=1
            temp = limit
        return boat
