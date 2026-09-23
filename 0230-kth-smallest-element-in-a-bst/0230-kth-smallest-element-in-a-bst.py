# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        curr = root
        while curr:
            if curr.left is None:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right is None:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1
