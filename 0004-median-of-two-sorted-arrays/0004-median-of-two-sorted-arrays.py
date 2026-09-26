class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        lst.sort()

        n = len(lst)

        if n % 2 == 1:
            return lst[n // 2]
        else:
            return (lst[n // 2 - 1] + lst[n // 2]) / 2
        