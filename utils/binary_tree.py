class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # DFS = Pre Order Traversal
    def preorder_traversal(self, root):
        # Root -> Left -> Right
        if root == None:
            return None

        # to_return += str(root.value)  + "-"
        print(str(root.value) + "-> ", end = '')

        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

        print("final")

    def bfs(self, root):

        if root == None:
            return None

        queu = []
        queu.append(root)

        while len(queu) > 0:

            node = queu.pop(0)

            print(node.value)

            if node.left != None:
                queu.append(node.left)


            if node.right != None:
                queu.append(node.right)
        return 




        





if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    # tree.preorder_traversal(tree.root)
    tree.bfs(tree.root)
