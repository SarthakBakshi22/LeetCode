class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return result
        rowStart = 0
        colStart = 0
        maxRows = len(matrix)-1 
        maxCols = len(matrix[0])-1
        while (rowStart <= maxRows and colStart <= maxCols):
            for i in range(colStart,maxCols+1):
                result.append(matrix[rowStart][i])
            rowStart += 1
            for i in range(rowStart,maxRows+1):
                result.append(matrix[i][maxCols])
            maxCols -= 1
            if (rowStart <= maxRows):
                for i in range(maxCols,colStart-1,-1):
                    result.append(matrix[maxRows][i])
                maxRows -= 1
            if (colStart <= maxCols):
                for i in range(maxRows,rowStart-1,-1):
                    result.append(matrix[i][colStart])
                colStart += 1
        return result
