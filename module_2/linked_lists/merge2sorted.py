# Definition for singly-linked list.
# Constraints: we can't create copies of the node.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # we create a dummy node to avoid the edge case.
        dummy = ListNode()
        
        tail = dummy

        while (l1 != None) and (l2 != None):
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
                
        if l1 != None:
            tail.next = l1
            
        elif l2 != None:
            tail.next = l2

        return dummy.next




if __name__ == "__main__":
    solution = Solution()