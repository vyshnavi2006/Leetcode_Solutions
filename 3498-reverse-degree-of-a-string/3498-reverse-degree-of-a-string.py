class Solution:
    def reverseDegree(self, s: str) -> int:
        tot = 0
        i=0
        for i in range(len(s)):
            tot += (26-(ord(s[i])-ord('a')))*(i+1)
            i+=1

        return tot
        