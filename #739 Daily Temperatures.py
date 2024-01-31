class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:

        days_count = len(T)

        next_warm_day = [0 for _ in range(days_count)]

        for d in range(days_count - 2, -1, -1):

            next_day = 1
            while next_day and T[d + next_day] <= T[d]: # while next_node and next_node.val <= curr_node.val
                if next_warm_day[d + next_day]:
                    next_day += next_warm_day[d + next_day]
                
                else:
                    next_day = 0
            next_warm_day[d] = next_day
        
        return next_warm_day
            
