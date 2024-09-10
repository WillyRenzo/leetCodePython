import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current_node = head
        previous_node = head
        
        while(current_node.next is not None):
            next_node = current_node.next
            
            result = math.gcd(current_node.val, next_node.val)
            new_node = ListNode(result, next_node)
            
            current_node.next = new_node
            previous_node = current_node
            current_node = current_node.next.next
            
        return head
