# Definition for singly-linked list.
# https://www.youtube.com/watch?v=G0_I-ZF0S38

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        current = head
        previus = None

        while current:
            # save this value, cuz we are going to modify it
            n= current.next
            
            # main idea
            
            current.next = previus
            previus = current 
            current = n
            
        return previus
        

##### THERE IS A RECURSIVE WAY TO DO THIS. 







if __name__ == "__main__":
    solution = Solution()