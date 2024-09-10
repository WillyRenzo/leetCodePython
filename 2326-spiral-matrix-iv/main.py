# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        """
        Generates an m x n matrix containing integers from a linked list in spiral order.

        Args:
            m: Number of rows in the matrix.
            n: Number of columns in the matrix.
            head: Head of the linked list.

        Returns:
            The generated m x n matrix.
        """

        matrix = [[-1] * n for _ in range(m)]
        row_start, row_end, col_start, col_end = 0, m - 1, 0, n - 1
        curr = head

        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for i in range(col_start, col_end + 1):
                if curr:
                    matrix[row_start][i] = curr.val
                    curr = curr.next
                else:
                    break
            row_start += 1

            # Traverse down
            for i in range(row_start, row_end + 1):
                if curr:
                    matrix[i][col_end] = curr.val
                    curr = curr.next
                else:
                    break
            col_end -= 1

            # Traverse left
            for i in range(col_end, col_start - 1, -1):
                if curr:
                    matrix[row_end][i] = curr.val
                    curr = curr.next
                else:
                    break
            row_end -= 1

            # Traverse up
            for i in range(row_end, row_start - 1, -1):
                if curr:
                    matrix[i][col_start] = curr.val
                    curr = curr.next
                else:
                    break
            col_start += 1

        return matrix
        