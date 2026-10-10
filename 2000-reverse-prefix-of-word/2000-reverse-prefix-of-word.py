class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack =[]
        ans = []
        cnt=0
        for i in word:
            if ch not in word:
                return word
        for i in word:
            if i != ch:
                stack.append(i)
                cnt+=1
            else:
                stack.append(i)
                break
        while len(stack)>0:
            ans.append(stack[-1])
            stack.pop()
        for i in range(cnt+1,len(word)):
            ans.append(word[i])
        s = ''.join(ans)
        return s


        