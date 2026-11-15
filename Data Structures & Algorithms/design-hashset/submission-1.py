class MyHashSet:

    def __init__(self):
        self.nums = []

    def add(self, key: int) -> None:
        for num in self.nums:
            if num == key:
                return  None
        self.nums.append(key)

    def remove(self, key: int) -> None:
        for index,value in enumerate(self.nums):
            if value == key:
                del self.nums[index]


    def contains(self, key: int) -> bool:
        for num in self.nums:
            if num == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)