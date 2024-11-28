'''Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def dfs(node):
            if not node:
                return 
                
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)

        dfs(root)
        return nodes