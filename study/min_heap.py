class MinHeap:
    """
    A complete Min Heap implementation.
    The smallest element is always at the root.
    """
    
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def peek(self):
        """Return minimum without removing it."""
        if self.is_empty():
            return None
        return self.data[0]
    
    # Index calculations
    def _parent_index(self, i):
        return (i - 1) // 2
    
    def _left_child_index(self, i):
        return 2 * i + 1
    
    def _right_child_index(self, i):
        return 2 * i + 2
    
    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    # Core operations
    def push(self, value):
        """Insert a new element. O(log n)"""
        self.data.append(value)
        self._bubble_up(len(self.data) - 1)
    
    def pop(self):
        """Remove and return minimum. O(log n)"""
        if self.is_empty():
            return None
        
        if len(self.data) == 1:
            return self.data.pop()
        
        minimum = self.data[0]
        self.data[0] = self.data.pop()
        self._bubble_down(0)
        
        return minimum
    
    def _bubble_up(self, index):
        while index > 0:
            parent_idx = self._parent_index(index)
            if self.data[parent_idx] <= self.data[index]:
                break
            self._swap(index, parent_idx)
            index = parent_idx
    
    def _bubble_down(self, index):
        size = len(self.data)
        
        while True:
            smallest = index
            left = self._left_child_index(index)
            right = self._right_child_index(index)
            
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest


# Complete test
print("=== MIN HEAP TEST ===\n")

heap = MinHeap()

# Insert elements
elements = [15, 10, 20, 17, 8, 25]
print(f"Inserting: {elements}\n")

for elem in elements:
    heap.push(elem)
    print(f"  push({elem}) -> heap: {heap}")

print(f"\nMinimum (peek): {heap.peek()}")
print(f"Heap size: {len(heap)}\n")

# Extract all elements
print("Extracting all elements:")
while not heap.is_empty():
    print(f"  pop() -> {heap.pop()}")
# ```

# ---

# ## Part 7: Complexities

# | Operation | Complexity | Why? |
# |-----------|------------|------|
# | `peek()` | O(1) | Just access index 0 |
# | `push()` | O(log n) | Bubble up at most tree height |
# | `pop()` | O(log n) | Bubble down at most tree height |
# | `len()` | O(1) | Python stores the size |

# The height of a complete binary tree with `n` elements is `log₂(n)`.

# ---

# ## Visual Summary
# ```
# PUSH (insert 1):
# [3, 5, 4] -> [3, 5, 4, 1] -> [1, 3, 4, 5]
#              add to end      bubble up

# POP (extract minimum):
# [1, 3, 4, 5] -> [5, 3, 4] -> [3, 5, 4]
#  save 1         move last    bubble down
#                 to root
# ```