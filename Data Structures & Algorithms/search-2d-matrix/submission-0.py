class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix) - 1
        while left_row <= right_row:
            middle_row = (left_row + right_row) // 2
            if target >= matrix[middle_row][0] and target <= matrix[middle_row][len(matrix[0]) - 1]:
                break
            elif target < matrix[middle_row][0]:
                right_row = middle_row - 1
            elif target > matrix[middle_row][len(matrix[0]) - 1]:
                left_row = middle_row +1
        left_col = 0
        right_col = len(matrix[0]) - 1
        while left_col <= right_col:
            middle_col = (left_col + right_col) // 2
            if target == matrix[middle_row][middle_col]:
                return True
            elif target > matrix[middle_row][middle_col]:
                left_col = middle_col + 1
            else:
                right_col = middle_col - 1
        return False
