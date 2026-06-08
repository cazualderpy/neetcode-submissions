class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for element in s:
            s_count[element] = s_count.get(element, 0) + 1

        for element in t:
            t_count[element] = t_count.get(element, 0) + 1

        return s_count == t_count