class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                return(self.search(row,target))
        return False

    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1
        while l <=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid +1
        return False
 