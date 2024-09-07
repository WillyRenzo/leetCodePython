class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Helper function to check if linked list matches the path starting from the current tree node
        def dfs(node: TreeNode, head: ListNode) -> bool:
            # If the linked list is fully traversed, path exists
            if not head:
                return True
            # If the tree node is null or values don't match, return False
            if not node or node.val != head.val:
                return False
            # Recur on left and right subtrees
            return dfs(node.left, head.next) or dfs(node.right, head.next)

        # Main function to traverse the tree and check if any path matches the linked list
        if not root:
            return False
        # Start matching from the current node or traverse to left and right nodes
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)