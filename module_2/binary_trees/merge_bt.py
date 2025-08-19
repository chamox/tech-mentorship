class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return None
        if not root2:
            return root1
        
        merged = TreeNode(root1.value + root2.value)

        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged
    

# 100. Same Tree (misma forma/valores; cambia “sumar” por “comparar”).

# 226. Invert Binary Tree (actuar al visitar: swap).

# 572. Subtree of Another Tree (compara estructuras; hash o DFS).

# 563. Binary Tree Tilt / 2265 Average of Subtree (DP por subárbol con tuplas).

# 617. Merge Two Binary Trees (éste).