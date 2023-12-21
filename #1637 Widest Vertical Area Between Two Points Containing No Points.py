class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        x_axis = []

        for i in points:
            x_axis.append(i[0])
        
        x_axis.sort()

        max_width = 0

        for i in range(len(x_axis)-1):
            width = x_axis[i+1]-x_axis[i]

            max_width = max(max_width,width)
        
        return max_width
        
