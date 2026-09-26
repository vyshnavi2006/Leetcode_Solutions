class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        cnt =0
        
        while(j<len(t) and i < len(s)):
            if s[i] == t[j]:
                cnt+=1
                j+=1
                i+=1
            else:
                j+=1
        if len(s) == cnt:
            return True
        else:
            return False
            






        