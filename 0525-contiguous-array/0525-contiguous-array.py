class Solution:
    def findMaxLength(self, nums):
        freq = {0: -1}
        total = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1

            if total in freq:
                length = i - freq[total]
                ans = max(ans, length)
            else:
                freq[total] = i

        return ans