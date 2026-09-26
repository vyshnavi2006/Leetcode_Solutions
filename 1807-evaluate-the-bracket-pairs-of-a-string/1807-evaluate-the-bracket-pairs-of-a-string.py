class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = {}
        for key, value in knowledge:
            mp[key] = value
        ans = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""
                while s[i] != ')':
                    key += s[i]
                    i += 1
                if key in mp:
                    ans += mp[key]
                else:
                    ans += "?"
            else:
                ans += s[i]
            i += 1
        return ans