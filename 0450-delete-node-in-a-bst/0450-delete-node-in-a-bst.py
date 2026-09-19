class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        if root is None:
            return None

        if root.val == key:
            return self.deletion(root)

        temp = root

        while temp is not None:

            if temp.val > key:

                if temp.left is not None and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left

            else:

                if temp.right is not None and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right

        return root

    def deletion(self, node: TreeNode):

        # Case 1: No left child
        if node.left is None:
            return node.right

        # Case 2: No right child
        elif node.right is None:
            return node.left

        # Case 3: Both children exist
        else:
            rightchild = node.right

            lastright = self.findLastRight(node.left)

            lastright.right = rightchild

            return node.left

    def findLastRight(self, node: TreeNode):

        while node.right is not None:
            node = node.right

        return node