class Solution:
    def longestPalindrome(self, s: str) -> int:
        fre = Counter(s)
        cnt = 0
        cntt=0
        for let,freq in fre.items():
            if freq % 2 == 0:
                cnt+=freq
            else:
                cnt+=freq-1
                cntt+=1
        if cntt>=1:
            return cnt+1
        else:
            return cnt
        