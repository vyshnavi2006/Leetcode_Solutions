class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        tot = 0

        for i in range(len(nums)):
            tot += maxi - nums[i]

        return tot