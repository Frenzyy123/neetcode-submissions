class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrixSum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            rowSum = 0
            for j in range(len(matrix[0])):
                rowSum += matrix[i][j]
                self.matrixSum[i + 1][j + 1] = rowSum + self.matrixSum[i][j + 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        wholeSquare = self.matrixSum[row2][col2]
        left = self.matrixSum[row2][col1 - 1]
        above = self.matrixSum[row1 - 1][col2]
        common_part = self.matrixSum[row1 - 1][col1 - 1]
        return wholeSquare - left - above + common_part


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)