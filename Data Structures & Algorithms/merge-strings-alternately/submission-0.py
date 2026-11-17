class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2 = 0,0
        solution = ""
        while l1 <= len(word1)-1 and l2 <= len(word2)-1:
            solution += word1[l1]
            solution += word2[l2]
            l1+=1
            l2+=1
        solution += word1[l1:] + word2[l2:]
        return solution
        

        