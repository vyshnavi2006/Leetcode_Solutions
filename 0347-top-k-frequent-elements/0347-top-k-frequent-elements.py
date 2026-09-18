class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        res = sorted(freq, key=lambda x: freq[x], reverse=True)

        return res[:k]