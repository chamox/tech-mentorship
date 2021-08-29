# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # HOW TO TRAVERSE A BINARY TREE?

    ###############################
    ###### DFS RECURSIVE WAY ######
    ###############################

    # Pre-order traversal
    def printPreOrder(self, root):

        if root == None:
            return 0
        else:
            print(root.val)
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)


    # Post-order traversal
    def printPostOrder(self, root):

        if root == None:
            return 0
        else:
            
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.val)

    # In-order traversal
    def printInOrder(self, root):

        if root == None:
            return 0
        else:
            
            self.printInOrder(root.left)
            print(root.val)
            self.printInOrder(root.right)

    # Breadth-First Search (BFS)   


    ###############################
    ###### BFS ITERATIVE WAY ######
    ###############################

    # Level Order     
    def BFS(self, root):
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

                print(node.val)

                # If we have a left child, we enqueue it 
                if node.left != None:
                    queue.append(node.left)

                # If we have a right child, we enqueue it 
                if node.right != None:
                    queue.append(node.right)


    ###############################
    ###### DFS ITERATIVE WAY ######
    ###############################


    
    # Pre order traversal
    def DFS(self, root):
        if root == None:
            return 0

        else:
            stack = list()

            # First of all, we put our root into a stack
            stack.append(root)

            # Now we start the algorithm

            while len(stack) != 0:
                # Remember, in queues we respect FIFO, so we remove the first element in
                node = stack.pop()

                print(node.val)               

                # If we have a right child, we enqueue it 
                if node.right != None:
                    stack.append(node.right)

                # If we have a left child, we enqueue it 
                if node.left != None:
                    stack.append(node.left)



if __name__ == "__main__":

    #       1
    #   2       3
    # 4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.printPreOrder(root)
