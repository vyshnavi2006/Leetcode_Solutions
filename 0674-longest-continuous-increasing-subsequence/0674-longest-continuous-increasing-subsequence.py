class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        maxi = 1
        cnt = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cnt +=1
                maxi = max(maxi,cnt)
            else:
                cnt=1
        return maxi
