class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    result.append((i,j))
        for tup in result:
            for i in range(len(matrix)):
                matrix[i][tup[1]] = 0
            for j in range(len(matrix[0])):
                matrix[tup[0]][j] = 0
