class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lengthMatrix = len(matrix) 
        counter = 0
        while counter < lengthMatrix:
            l,r = 0, len(matrix[counter]) - 1 
            while l <= r:
                mid = (l+r)//2

                if matrix[counter][mid] < target:  
                    l = mid +1
                elif matrix[counter][mid]> target:
                    r = mid - 1
                else:
                    return True
            counter +=1
        return False

