class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] < 0:
                nums[i] = abs(nums[i])

        nums.sort(reverse=True)
        tot = 0
        n = (len(nums)+1) // 2

        for i in range(0, n):
            tot += pow(nums[i], 2)

        for i in range(n, len(nums)):
            tot -= pow(nums[i], 2)

        return tot
