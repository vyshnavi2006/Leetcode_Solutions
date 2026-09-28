class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        maxi = 0
        for ch in s:
            if ch == '(':
                cnt += 1
                maxi = max(maxi,cnt)
            elif ch == ')':
                cnt -= 1
        return maxi