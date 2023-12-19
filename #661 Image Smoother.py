class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])

        new_img = [[0 for i in range(n)] for j in range(m)]

        def checkVaidPlace(i,j):
            if i>=0 and i<m and j>=0 and j<n:
                return 1
            return 0

        def checkValid(i,j):
            if i>=0 and i<m and j>=0 and j<n:
                return img[i][j]
            return 0


        def new_(i,j):
            s = checkValid(i,j) + checkValid(i-1,j) + checkValid(i+1,j) + checkValid(i,j-1) + checkValid(i,j+1) + checkValid(i-1,j-1) + checkValid(i-1,j+1) + checkValid(i+1,j-1) + checkValid(i+1,j+1)

            t = checkVaidPlace(i,j) + checkVaidPlace(i-1,j) + checkVaidPlace(i+1,j) + checkVaidPlace(i,j-1) + checkVaidPlace(i,j+1) + checkVaidPlace(i-1,j-1) + checkVaidPlace(i-1,j+1) + checkVaidPlace(i+1,j-1) + checkVaidPlace(i+1,j+1)

            new_img[i][j] = s//t

        for i in range(m):
            for j in range(n):
                new_(i,j)

        return new_img
