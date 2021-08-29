# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # this is a sentinel node, we avoid edge cases
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        current = dummy.next
        
        
        # while our current node exists
        while current:
            
            # if we have a next node, and that node has the same value as our current
            if current.next != None and current.val == current.next.val:
                
                # we check the consecutive same values
                while current.next and current.val == current.next.val:
                    current = current.next
                    
                prev.next = current.next
                       
            else:
                # if consecutive nodes have not the same value or the second one is the last
                prev = prev.next
                
            current=current.next
            
        return dummy.next              
     
            
 