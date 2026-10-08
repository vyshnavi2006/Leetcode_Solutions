class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        for ch in s:
            if ch == '(':
                if len(stack)> 0:
                    result.append(ch)
                stack.append(ch)
            else:
                stack.pop()
                if len(stack)>0:
                    result.append(ch)
        return ''.join(result)

        