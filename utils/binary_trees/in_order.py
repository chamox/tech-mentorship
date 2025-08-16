class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
        result = []
        
        def inorder(node):
            if node:
                inorder(node.left)      # 1. Procesar izquierda COMPLETA
                result.append(node.val) # 2. Procesar nodo actual
                inorder(node.right)     # 3. Procesar derecha COMPLETA
        
        inorder(root)
        return result

    def inorderTraversalIterative(self, root):
        result = []
        stack = []
        current = root
        
        while stack or current:
            # Fase 1: Ir lo más a la IZQUIERDA posible
            while current:
                stack.append(current)   # "Recordar" este nodo para después
                current = current.left  # Seguir bajando a la izquierda
            
            # Fase 2: Procesar el nodo más a la izquierda
            current = stack.pop()       # Sacar el nodo que guardamos
            result.append(current.val)  # AHORA sí lo procesamos
            
            # Fase 3: Ir al subárbol derecho
            current = current.right     # Explorar la derecha
        
        return result
    


# LeetCodes recomendados (por objetivo)
# Fundamento (inorden en sí):

# 94. Binary Tree Inorder Traversal — práctica pura de recorrido (hazlo recursivo e iterativo).

# Orden ascendente / propiedades de BST:

# 98. Validate Binary Search Tree — usa inorden creciente o límites [low, high].

# 230. Kth Smallest in a BST — inorden con corte temprano (ideal iterativo).

# 783. Minimum Distance Between BST Nodes (o 530. Minimum Absolute Difference) — compara adyacentes del inorden.

# 653. Two Sum IV – Input is a BST — inorden → dos punteros (o dos iteradores, uno ascendente y otro descendente).

# 173. Binary Search Tree Iterator — materializa el patrón de inorden perezoso.

# Reverse Inorder / transformaciones:

# 538/1038. Convert BST to Greater Tree — reverse inorder con acumulador global.

# 897. Increasing Order Search Tree — inorden para rehacer el árbol inclinado a la derecha.

# 99. Recover Binary Search Tree — detecta 1–2 inversiones en el orden inorden (dos “roturas”).

# (Opcionales si te topas con premium / variantes: 285 “Inorder Successor in BST”, 510 “Inorder Successor II”).