# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: ListNode) -> ListNode:
        nums = set(nums) 
        current_node = head
        previous_node = head
        while current_node is not None:
            if head.val in nums:
                head = head.next
                current_node = head
                continue

            if current_node.val in nums:
                previous_node.next = current_node.next
                current_node = current_node.next
                continue
    
            previous_node = current_node
            current_node = current_node.next
        
        return head