class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i,j = 0,len(s)-1
        while(i<j):
            ch1 = s[i]
            ch2 = s[j]
            if not ch1.isalpha():
                i+=1
            elif not ch2.isalpha():
                j-=1
            else:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1
        return ''.join(s)
            