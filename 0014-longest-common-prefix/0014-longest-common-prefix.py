class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre =strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(pre):
                pre =pre[:-1]
                if pre == "":
                    return ""
        return pre
        