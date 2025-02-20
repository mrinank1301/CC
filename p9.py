#Write a Program to Swap Nodes pairwise.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        
        # Swapping
        first.next = second.next
        second.next = first
        prev.next = second
        
        # Move to the next pair
        prev = first
    
    return dummy.next

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example Usage
if __name__ == "__main__":
    # Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print("Original List:")
    printList(head)
    
    new_head = swapPairs(head)
    
    print("Swapped List:")
    printList(new_head)
