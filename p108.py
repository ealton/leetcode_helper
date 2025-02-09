# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 2:
            return TreeNode(nums[0], right=TreeNode(nums[1]))
        if len(nums) == 3:
            return TreeNode(nums[1], left=TreeNode(nums[0]), right=TreeNode(nums[2]))

        mid = len(nums) // 2
        return TreeNode(nums[mid], left=self.sortedArrayToBST(nums[:mid]), right=self.sortedArrayToBST(nums[mid+1:]))