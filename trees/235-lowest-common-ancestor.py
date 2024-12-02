'''Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # case 1 is if n1 < root <2 : return root 
        # case if root == either one of the nodes: return root 
        # lca is either root, in left subtree or right subtree
        # if both nodes > root, go to right subtree to find lca 
        # if both nodes < root, go to left subtree to find lca 
        def recursive_bca(root, p, q):
            if p <= root.val <= q:
                return root.val
            if p > root.val and q > root.val:
                return recursive_bca(root.right, p, q)
            if p < root.val and q < root.val:
                return recursive_bca(root.left, p, q)

        
        p, q = min(p.val, q.val), max(p.val, q.val)
        return recursive_bca(root, p, q)