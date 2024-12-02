'''Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # has_p = {}
        # has_q = {}
        # answer = root
        # def mark_tree_p(root):
        #     if not root:
        #         return False
        #     if root.val == p.val:
        #         has_p[root.val] = True
        #         return True
        #     has_p[root.val] = mark_tree_p(root.left) or mark_tree_p(root.right)
        #     return has_p[root.val]

        # def mark_tree_q(root):
        #     if not root:
        #         return False
        #     if root.val == q.val:
        #         has_q[root.val] = True
        #         return True
        #     has_q[root.val] = mark_tree_q(root.left) or mark_tree_q(root.right)
        #     return has_q[root.val]
        
        # def find_lca(root):
        #     nonlocal answer
        #     if not root:
        #         return 
        #     if root.val not in has_q or root.val not in has_p or not has_q[root.val] or not has_p[root.val]:
        #         return
        #     answer = root
        #     find_lca(root.left)
        #     find_lca(root.right)
        
        # mark_tree_p(root)
        # mark_tree_q(root)

        # find_lca(root)
        # return answer

        '''Intuition for first solution: 
        loop through the tree, saving whether node contains p or q in a map
        then, final recurse tree down to find node that has both p and q and set global answer 
        '''


        answer = root
        isSet = False
        def recurse(node):
            nonlocal answer
            nonlocal isSet
            if isSet:
                return False, False
            if not node:
                return False, False 
            found_p = False 
            found_q = False 
            if node.val == p.val:
                found_p = True
            elif node.val == q.val:
                found_q = True 
            left = recurse(node.left)
            right = recurse(node.right)
            found_p = found_p or left[0] or right[0]
            found_q = found_q or left[1] or right[1]
            if found_p and found_q:
                answer = node
                isSet = True
                return False, False
            return found_p, found_q
        
        recurse(root)
        return answer

        '''
        for each node, found p and found q is False 
        if the node is p or q, we set to True 
        then, left = search through left tree for p and q 
        then, right = search through right tree for p and q
        then found p would be leftp or rightp
        found q would be leftq or rightq 
        base case 
        return False False
        When a node is found to be p or q, we make sure to return True 
        the moment found p and found q is true, set answer to node, and isSet to True
        return False False to prune search
        '''