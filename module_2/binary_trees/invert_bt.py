# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root == None:
            return 0

        else:
            
            l = root.left
            r = root.right

            root.left = r
            root.right = l

            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root


    def InvertTreeBFS(self, root):
        if root == None:
            return 0

        else:
            queue = list()

            # First of all, we put our root into the queue
            queue.append(root)

            # Now we start the algorithm

            while len(queue) != 0:
                # Remember, in queues we respect FIFO, so we remove the first element in
                node = queue.pop(0)

                l = node.left 
                r = node.right
                
                node.left = r
                node.right = l

                # If we have a left child, we enqueue it 
                if node.left != None:
                    queue.append(node.left)

                # If we have a right child, we enqueue it 
                if node.right != None:
                    queue.append(node.right)
            return root

    # DFS 
    def printPreOrder(self, root):

        if root == None:
            return 0
        else:
            print(root.val)
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

if __name__ == "__main__":

        #       1
        #   2       3
        # 4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    sol.printPreOrder(root)