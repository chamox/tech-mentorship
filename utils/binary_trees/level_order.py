class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        
        result = []
        queue = [root]  # Lista normal como cola
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Procesar todos los nodos del nivel actual
            for i in range(level_size):
                node = queue.pop(0)  # Saca el PRIMERO (simula popleft)
                current_level.append(node.val)
                
                # Agregar hijos para el siguiente nivel
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
    
# Básicos (calentamiento)
# 102. Binary Tree Level Order Traversal — salida por niveles (lista de listas).

# 107. Binary Tree Level Order Traversal II — igual que 102, pero de abajo hacia arriba.

# 103. Binary Tree Zigzag Level Order Traversal — alterna izquierda↔derecha por nivel.

# Vistas y extremos del nivel
# 199. Binary Tree Right Side View — toma el último del nivel.

# 513. Find Bottom Left Tree Value — último nivel, primer nodo.

# Agregados y métricas por nivel
# 637. Average of Levels in Binary Tree — promedio por nivel.

# 515. Find Largest Value in Each Tree Row — máximo por nivel.

# 1161. Maximum Level Sum of a Binary Tree — nivel con mayor suma.

# 1302. Deepest Leaves Sum — suma de hojas más profundas.

# 1609. Even Odd Tree — reglas por nivel (par/impar), buen control de “por nivel”.

# Distancias / profundidad (corte temprano)
# 111. Minimum Depth of Binary Tree — para en la primera hoja.

# 863. All Nodes Distance K in Binary Tree — BFS desde “target” tras mapear padres (árbol como grafo).

# Anchos, índices y estructura
# 662. Maximum Width of Binary Tree — índices por nivel (estilo heap) y normalización.

# 958. Check Completeness of a Binary Tree — completitud con BFS (tras ver un “hueco”, no deben venir más nodos).

# Conectar hermanos (mismo nivel)
# 116. Populating Next Right Pointers in Each Node — árbol perfecto.

# 117. Populating Next Right Pointers in Each Node II — caso general.

# Columnas / vertical (BFS con metadatos)
# 314. Binary Tree Vertical Order Traversal (premium) — agrupa por columna con BFS para estabilidad de orden.

# 987. Vertical Order Traversal of a Binary Tree — vertical con ordenamientos finos (más exigente).

# Extra (no binario pero útil para afianzar BFS)
# 429. N-ary Tree Level Order Traversal — misma idea en árboles N-arios.

# Ruta sugerida (8 pasos)
# 102 → 107 → 199 → 111 → 637 → 515 → 662 → 958
# (opcional luego: 116/117, 1302, 1609, 314/987, 863)

# Si quieres, elegimos uno ahora (p. ej., 199 o 111) y lo resolvemos paso a paso con la plantilla de nivel + el truco específico.