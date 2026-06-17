class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix = [[0] * 4 for i in range(3)]
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                continue
            elif matrix[i][0] > target:
                return target in matrix[i-1]
        return target in matrix[len(matrix)-1]
