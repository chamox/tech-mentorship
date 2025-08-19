# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if (p is None) and (q is None):
            return True 

        if (p is None) or (q is None):
            return False 

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
        

# “Primos” del mismo patrón (para reforzar)

# 617. Merge Two Binary Trees: cambia “comparar” por “sumar y unir”.

# 101. Symmetric Tree: compara en espejo (izq con der y der con izq).

# 572. Subtree of Another Tree: busca si alguno de los subárboles de s es “same tree” con t.