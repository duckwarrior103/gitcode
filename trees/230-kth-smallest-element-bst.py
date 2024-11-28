'''Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # current = 0  # Keeps track of the number of nodes visited
        # answer = None  # Stores the k-th smallest value
        
        # def dfs(node):
        #     nonlocal current, answer
        #     if not node:
        #         return  # Base case: If the node is None, return
            
        #     # In-order traversal: left -> node -> right
        #     if node.left:
        #         dfs(node.left)
        #         if current == k:  # Stop recursion once answer is found
        #             return

        #     current += 1  # Increment count for the current node
        #     if current == k:  # Check if this is the k-th node
        #         answer = node.val
        #         return
            
        #     if node.right:
        #         dfs(node.right)
        #         if current == k:  # Stop recursion once answer is found
        #             return

        # dfs(root)  # Start in-order traversal from the root
        # return answer

        # iterative solution

        values = []
        traverse = [(root, False)]
        while traverse:
            node, visited = traverse.pop()
            if not node:
                continue
            if visited:
                values.append(node.val)
                if len(values) == k:
                    break
                continue
            traverse.append((node.right, False))
            traverse.append((node, True))
            traverse.append((node.left, False))


        return values[-1]
