class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        zaehler = defaultdict(int)
        for num in nums:
            zaehler[num] += 1
        anzahl = sorted(zaehler.items(), key=lambda w: w[1], reverse=True)
        return [zahl for zahl, haeufigkeit in anzahl[:k]]