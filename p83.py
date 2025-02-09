# Definition for a binary tree node.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current = head
        previous = head
        while current.next is not None:
            if current.next.val == current.next:
                current = current.next
                continue

            previous.next = current.next
            current = current.next
            previous = current.next
        previous.next = None
        return head
