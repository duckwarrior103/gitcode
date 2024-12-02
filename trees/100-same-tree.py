'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def recursive_check(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return recursive_check(t1.left, t2.left) and recursive_check(t1.right, t2.right)

        return recursive_check(p, q)