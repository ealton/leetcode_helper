# Definition for a binary tree node.
from typing import Optional, List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def duplicateList(nums: List[int]):
            new_list = []
            for item in nums:
                new_list.append(item)
            return new_list

        def helper(nums: List[int]):
            # print(f'helper: {nums}')

            if len(nums) == 1:
                return [nums]

            result_list = helper(nums[1:])
            # print(f'result_list = {result_list}')
            for i in range(len(result_list)):
                # print(f'loop, item = {result_list[i]}')
                temp_list = duplicateList(result_list[i])
                temp_list.insert(0, nums[0])
                if temp_list not in result_list:
                    result_list.append(temp_list)

            if [nums[0]] not in result_list:
                result_list.insert(0, [nums[0]])
            return result_list

        result = helper(nums)
        result.append([])
        return result
