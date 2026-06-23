class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for wert in nums:
            if wert != val:
                nums[k] = wert
                k += 1
        return k
            
