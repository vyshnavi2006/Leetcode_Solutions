class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        total = 0
        cnt = 0
        for x in nums:
            total += x
            if total - k in freq:
                cnt += freq[total - k]
            freq[total] = freq.get(total, 0) + 1
        return cnt