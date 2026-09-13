class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix) - 1
        while left_row <= right_row:
            target_row = (left_row + right_row) // 2
            if target >= matrix[target_row][0] and target <= matrix[target_row][len(matrix[0]) - 1]:
                break
            elif target < matrix[target_row][0]:
                right_row = target_row - 1
            else:
                left_row = target_row + 1
        left_col = 0
        right_col = len(matrix[0]) - 1 
        while left_col <= right_col:
            target_col = (left_col + right_col) // 2
            if target == matrix[target_row][target_col]:
                return True
            elif target < matrix[target_row][target_col]:
                right_col = target_col - 1
            else:
                left_col = target_col + 1
        return False