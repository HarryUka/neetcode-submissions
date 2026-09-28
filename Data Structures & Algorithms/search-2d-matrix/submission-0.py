class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            left = matrix[r][0]
            right = matrix[r][cols - 1]
            if left <= target <= right:
                return self.binary_search(matrix[r],target)

        return False 


    def binary_search(self,arr,target):

        left , right = 0 , len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                return True 
        return False 


        