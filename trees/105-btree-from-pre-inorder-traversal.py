'''Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recurse(current_val, pre_nodes, in_nodes):
            ## create node 
            current_node = TreeNode(current_val)
            if len(pre_nodes) == len(in_nodes) == 1:
                return current_node

            ### find current val in in_nodes position
            i = 0
            while in_nodes[i] != current_val:
                i += 1
            # try to recurse left 
            if i == 0:
                current_node.left = None
            else:
                current_node.left = recurse(pre_nodes[1], pre_nodes[1:i+1], in_nodes[0:i])
            # try to recurse right
            if i == len(in_nodes) - 1:
                current_node.right = None
            else:
                current_node.right = recurse(pre_nodes[i+1], pre_nodes[i+1:len(in_nodes)], in_nodes[i+1:len(in_nodes)])
            return current_node
        return recurse(preorder[0], preorder, inorder)
        