class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = heights.copy()
        exp.sort()
        cnt = 0
        for i in range(0,len(heights)):
            if heights[i] != exp[i]:
                cnt+=1
        return cnt
        