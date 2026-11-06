class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        res = {}
        for i in nums2:
            while stack and stack[-1]<i:
                x = stack.pop()
                res[x] = i
            stack.append(i)
        while stack:
            res[stack.pop()]=-1
        ans = []
        for i in nums1:
            ans.append(res[i])
        return ans
