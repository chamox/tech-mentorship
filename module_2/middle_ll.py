# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        current = head
        
        hash_table = dict()
        
        c=1
        
        while current:
            
            hash_table[c]= current
            
            current = current.next
            
            if current:
                c+=1

        if (c%2 != 0):
            return hash_table[(c+1)//2]
        else:
            return hash_table[(c//2)+1]
            