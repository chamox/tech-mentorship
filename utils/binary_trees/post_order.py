class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def postorderTraversal(self, root):
        result = []
        
        def postorder(node):
            if node:
                postorder(node.left)    # 1. Procesar izquierda COMPLETA
                postorder(node.right)   # 2. Procesar derecha COMPLETA
                result.append(node.val) # 3. AHORA SÍ procesar nodo actual
        
        postorder(root)
        return result
    

    def postorderTraversalIterative(self, root):
        if not root:
            return []
        
        result = []
        stack = []
        current = root
        last_processed = None  # Variable extra para postorder
        
        while stack or current:
            # FASE 1: Ir a la izquierda hasta el fondo (igual que inorder)
            while current:
                stack.append(current)
                current = current.left
            
            # FASE 2: Revisar el nodo del tope (DIFERENTE a inorder)
            peek_node = stack[-1]  # Mirar sin sacar del stack
            
            # ¿Tiene hijo derecho que no hemos procesado?
            if peek_node.right and last_processed != peek_node.right:
                # Ir al subárbol derecho
                current = peek_node.right
            else:
                # Procesar este nodo (ambos hijos ya procesados)
                processed_node = stack.pop()
                result.append(processed_node.val)
                last_processed = processed_node
        
        return result
    


# LeetCodes recomendados (orden sugerido)
# Fundamentos de postorden:

# 145. Binary Tree Postorder Traversal — calienta motores (si quieres, iterativo con flag).

# DP bottom-up / propiedades de subárbol:

# 104. Maximum Depth of Binary Tree — altura simple con postorden.

# 110. Balanced Binary Tree — altura o -1 (corte temprano).

# 543. Diameter of Binary Tree — retorna altura y actualiza un global.

# 563. Binary Tree Tilt — retorna suma y acumula tilt.

# 2265. Count Nodes Equal to Average of Subtree — retorna (suma, conteo).

# Combinar hijos / decisiones en el padre:

# 236. Lowest Common Ancestor of a Binary Tree — booleans/refs que suben.

# 337. House Robber III — retorna (robo, no_robo).

# 968. Binary Tree Cameras (Hard) — DP por estados (cámara/cubierto/necesita).

# Estructura de subárboles:

# 652. Find Duplicate Subtrees — hashing postorden.

# 572. Subtree of Another Tree — hashing postorden o comparación desde cada raíz.

# (Opcionales avanzados: 124. Maximum Path Sum — excelente para afinar el patrón de “retorno vs. global”).