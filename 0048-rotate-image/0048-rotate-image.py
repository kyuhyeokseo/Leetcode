class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n>1:
            center = (n-1)/2
            i = 0
            while (i<center):
                j = 0
                while (j <= center):
                    di = center - i
                    dj = center - j
                    tmp = matrix[i][j]

                    matrix[i][j] = matrix[int(center+dj)][int(center-di)]
                    matrix[int(center+dj)][int(center-di)] = matrix[int(center+di)][int(center+dj)]
                    matrix[int(center+di)][int(center+dj)] = matrix[int(center-dj)][int(center+di)]
                    matrix[int(center-dj)][int(center+di)] = tmp

                    j += 1
                i += 1