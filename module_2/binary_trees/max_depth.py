# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # first of all, we need to traverse the tree given a root

        # termination condition
        if root == None:
            return 0

        else:

            left_tree = self.maxDepth(root.left)
            right_tree = self.maxDepth(root.right)

            # print(root.val)
            # print("left:",left_tree,"right",right_tree)

            return max(left_tree,right_tree) + 1
          

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()
    print(sol.maxDepth(root))