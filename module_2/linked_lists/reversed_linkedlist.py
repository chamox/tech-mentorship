# Definition for singly-linked list.
# https://www.youtube.com/watch?v=G0_I-ZF0S38

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # we are going to swap each node, the next one is going to be the previus, and the previus the next one
        # so, we start with a None because of the given head, where its next is going to be None (head is now the last node)

        # this is for the edge case: the head
        prev = None
        current = head

        while current != None:

            # we modify the current.next value after, so we save it.
            next_saved = current.next
            current.next = prev
            prev = current

            current = next_saved

        # Eventually, the current value is goint to be None, so we can't return that. We return the prev value, that is the new head.
        return prev    


##### THERE IS A RECURSIVE WAY TO DO THIS. 







if __name__ == "__main__":

    # setting example
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()

    reversed_list = solution.reverseList(head)

    print(10*"=")

    while reversed_list:
        actual_node = reversed_list.val
        print(actual_node)
        reversed_list =reversed_list.next



    






