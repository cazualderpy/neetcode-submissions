class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = ""
        for word in strs:
            solution += str(len(word)) + "#" + word
        return solution

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":                      # j läuft bis zum Trenner
                j += 1
            laenge = int(s[i:j])                    # Ziffern zwischen i und j
            res.append(s[j + 1 : j + 1 + laenge])   # String direkt nach dem #
            i = j + 1 + laenge
        return res

