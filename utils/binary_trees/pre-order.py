# ==============================================
# Preorder (N -> L -> R) — Simple class version
# ==============================================
# Idea:
#   Visit the node FIRST, then go Left, then Right.
# When to use:
#   - Serialize/clone/invert/flatten (act on parent before children)
#   - Combine with inorder to rebuild (preorder gives the root early)
# Complexity:
#   - Time: O(n)       — visit each node once
#   - Space: O(h)      — h = tree height (recursion or explicit stack)
# Pitfalls:
#   - Iterative: push RIGHT before LEFT (stack is LIFO)
#   - Recursive: base case for None
#
# Minimal node:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class PreorderTraversal:
    def __init__(self, root_node):
        self.root_node = root_node

    def traverse_recursive(self):
        result = []
        def visit_node(current_node):
            if current_node is None:
                return
            result.append(current_node.value)  # visit now (N)
            visit_node(current_node.left)      # then Left (L)
            visit_node(current_node.right)     # then Right (R)
        visit_node(self.root_node)
        return result

    def traverse_iterative(self):
        if self.root_node is None:
            return []
        result, node_stack = [], [self.root_node]
        while node_stack:
            current_node = node_stack.pop()
            result.append(current_node.value)       # visit now (N)
            if current_node.right is not None:      # push RIGHT first
                node_stack.append(current_node.right)
            if current_node.left is not None:       # then LEFT so it pops earlier
                node_stack.append(current_node.left)
        return result


# --- Tiny example (delete when memorized) ---
if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #        /
    #       4
    binary_tree = TreeNode(1, left=TreeNode(2), right=TreeNode(3, left=TreeNode(4)))
    preorder_traversal = PreorderTraversal(binary_tree)
    print("preorder recursive:", preorder_traversal.traverse_recursive())  # [1, 2, 3, 4]
    print("preorder iterative:", preorder_traversal.traverse_iterative())  # [1, 2, 3, 4]

    # LEETCODES
    # 297 https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
    # 226 https://leetcode.com/problems/invert-binary-tree/description/
    # 114 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    # 100 https://leetcode.com/problems/same-tree/
    # 105 https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    


# Casos típicos en LeetCode:

# Serializar/Deserializar (p. ej. 297; con marcadores None/#).

# Invertir un árbol (226): visitar y swap left/right al pasar.

# Flatten a lista enlazada (114): preservar orden raíz-izq-der.

# Reconstrucción con preorden + inorden: raíz primero te da el corte del inorden.

# Comparación/igualdad de árboles (100) como DFS directo (preorden suele ser cómodo).

# ⚠️ Cuándo NO usarlo típicamente:

# BST k-ésimo menor / validar BST → es Inorden el que te sirve.

# Altura/Diámetro/Balanceado → es Postorden (necesitas info de hijos).

# Mínima profundidad / vistas por nivel → BFS.