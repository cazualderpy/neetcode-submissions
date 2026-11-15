class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hashtable = defaultdict(list)
        for word in strs:
            sortierter_text = "".join(sorted(word))
            strs_hashtable[sortierter_text].append(word)

        return list(strs_hashtable.values())
