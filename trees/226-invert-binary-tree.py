'''Given the root of a binary tree, invert the tree, and return its root.

'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        backup = root 
        def recursive_swap(node):
            if not node:
                return
            node.left, node.right = node.right, node.left

            recursive_swap(node.left)
            recursive_swap(node.right)


        recursive_swap(root)
        return backup