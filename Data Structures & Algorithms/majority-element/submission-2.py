class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        eindeutigeliste = set(nums)
        solution = 0
        for num in eindeutigeliste:
            if nums.count(num) > len(nums)/2:
                solution = num 
        return solution
