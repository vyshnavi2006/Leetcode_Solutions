class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre=[1]*n
        su=[1]*n
        ans =[1]*n
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            su[i] = su[i+1]*nums[i+1]
        for i in range(0,len(nums)):
            ans[i] = pre[i]*su[i]
        return ans