# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Compute the effective rotation
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the new tail (length - k - 1) and new head (length - k)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Step 4: Rotate the list
        new_tail.next = None
        tail.next = head
        
        return new_head
