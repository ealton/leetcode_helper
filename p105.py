# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}: [l: ({self.left}), r: ({self.right})'

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)

    def helper(self, prestart, instart, inend, preorder, inorder):
        if prestart > len(preorder) - 1 or instart > inend:
            return None
        root = TreeNode(preorder[prestart])
        inindex = inorder.index(root.val)

        root.left = self.helper(prestart + 1, instart, inindex - 1, preorder, inorder)
        root.right = self.helper(prestart + inindex - instart + 1, inindex + 1, inend, preorder, inorder)

        return root