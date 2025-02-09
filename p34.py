from typing import List


class Solution:

    def test(self):
        # print(self.searchRange([5,7,7,8,8,10], 8))
        # print(self.searchRange([5,7,7,8,8,10], 6))
        # print(self.searchRange([], 0))
        # print(self.searchRange([1,2,2], 2))
        print(self.searchRange([1,2,3,3,3,3,4,5,9], 3))

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums:
        #     return [-1, -1]
        #
        # left, right = 0, len(nums) - 1
        #
        # while nums[left] < nums[right]:
        #     mid = (left + right) // 2
        #
        #     print(f'iteration: {left} {mid} {right}')
        #
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         # nums[mid] == target
        #         while nums[left] < target and nums[mid] == target:
        #             print(f'lmid = {mid}')
        #             if left == mid - 1:
        #                 left = mid
        #                 break
        #             mid = (left + mid) // 2
        #
        #         while nums[right] > target and nums[mid] == target:
        #             print(f'rmid = {mid}')
        #             if right == mid + 1:
        #                 right = mid
        #                 break
        #             mid = (mid + right) // 2
        #
        # return [left, right] if nums[left] == target else [-1, -1]

        # print(f'searchRange: {nums}')
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        l_index = -1
        r_index = -1
        mid_index = len(nums) // 2
        if nums[mid_index - 1] < target:
            result = self.searchRange(nums[mid_index:], target)
            if result[0] >= 0: l_index = result[0] + mid_index
            if result[1] >= 0: r_index = result[1] + mid_index
        elif nums[mid_index - 1] > target:
            l_index, r_index = self.searchRange(nums[0:mid_index], target)
        else:
            l_index, lr_index = self.searchRange(nums[0:mid_index], target)
            result = self.searchRange(nums[mid_index:], target)
            if result[1] >= 0:
                r_index = result[1] + mid_index
            r_index = max(lr_index, r_index)
        return [l_index, r_index]
