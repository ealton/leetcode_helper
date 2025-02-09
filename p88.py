from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cm = 0
        cn = 0
        new_array = []
        while cm < m or cn < n:
            if cm < m and cn < n:
                if nums1[cm] < nums2[cn]:
                    new_array.append(nums1[cm])
                    cm += 1
                else:
                    new_array.append(nums2[cn])
                    cn += 1
            elif cm >= m:
                new_array.append(nums2[cn])
                cn += 1
            else:
                new_array.append(nums1[cm])
                cm += 1
        for i in range(m+n):
            nums1[i] = new_array[i]
