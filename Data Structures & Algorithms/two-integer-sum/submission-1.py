class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        CountSum = {}
        solution = []
        for i, number in enumerate(nums):
            CountSum[i] = number
            for value in CountSum:
                if CountSum[i] + CountSum[value] == target and value != i:
                    solution = [value, i]
                    return solution