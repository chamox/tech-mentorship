# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        # MY FIRST SOLUTION
        
        # current = head        
        # hash_table = dict()        
        # c=1
        
        # while current:
            
        #     hash_table[c]= current            
        #     current = current.next
            
        #     if current:
        #         c+=1

        # if (c%2 != 0):
        #     return hash_table[(c+1)//2]
        # else:
        #     return hash_table[(c//2)+1]

        # ====================================
        # ====================================

        # PRO SOLUTION

        # we need two pointers, rabbit and turtle

        #this pointers goes at 2x speed
        rabbit = head

        #this pointer goes at normal speed
        turtle = head

        # so, we need to find the middle of the linked list

        while rabbit != None and rabbit.next != None:
            turtle = turtle.next
            rabbit = rabbit.next.next


        return turtle