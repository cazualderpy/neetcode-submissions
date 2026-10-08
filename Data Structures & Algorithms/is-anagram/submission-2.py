class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap1 = {}
        myMap2 = {}

        if len(s) != len(t):
            return False
        else:
            for char in s:
                if char in myMap1:
                    myMap1[char] += 1
                else:
                    myMap1[char] = 1
            for char in t:
                if char in myMap2:
                    myMap2[char] += 1
                else:
                    myMap2[char] = 1
        return myMap1 == myMap2