class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre,su = 0,0
        for i in range(0,n):
            pre = sum(nums[:i])
            su = sum(nums[i+1:])
            if pre == su:
                return i
        return -1