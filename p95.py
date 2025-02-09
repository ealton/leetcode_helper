# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(n: int, increment: int) -> List[TreeNode]:
            result = []
            if n == 1:
                return [TreeNode(1+increment)]
            for i in range(1, n+1):
                left_nodes = [] if i == 1 else helper(i - 1, increment)
                right_nodes = [] if i == n else helper(n - 1, increment + i)
                if len(left_nodes) == 0:
                    for right in right_nodes:
                        new_item = TreeNode(i+increment)
                        new_item.right = right
                        result.append(new_item)
                elif len(right_nodes) == 0:
                    for left in left_nodes:
                        new_item = TreeNode(i+increment)
                        new_item.left = left
                        result.append(new_item)
                else:
                    for left in left_nodes:
                        for right in right_nodes:
                            new_item = TreeNode(i+increment)
                            new_item.left = left
                            new_item.right = right
                            result.append(new_item)
            return result

        return helper(n, 0)