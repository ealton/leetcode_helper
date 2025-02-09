from typing import List


class Solution:

    def test(self):
        print(self.findMin([4,5,6,7,0,1,2]))
        print(self.findMin([3,4,5,1,2]))
        print(self.findMin([11,13,15,17]))
        # a = 0

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r - l > 1:
            m = (r + l) // 2
            if nums[r] < nums[m]:
                l = m
            else:
                r = m

        if r > l:
            return min(nums[r], nums[l])
        return nums[r]
