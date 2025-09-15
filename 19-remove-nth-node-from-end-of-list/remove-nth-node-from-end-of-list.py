# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node before head to handle edge cases
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next

        # Delete nth node
        slow.next = slow.next.next

        return dummy.next
