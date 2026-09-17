class Solution:
    def maxPower(self, s: str) -> int:
        cnt = 1
        maxi = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cnt +=1
            else:
                maxi = max(maxi,cnt)
                cnt = 1
            maxi = max(maxi,cnt)
        return maxi
        