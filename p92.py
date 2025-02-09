# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head

        left -= 1
        right -= 1

        left_previous = None
        left_cursor = None
        right_next = None

        current_index = 0
        cursor = head

        center_link = None

        while cursor is not None:
            if current_index + 1 == left:
                left_previous = cursor
                left_cursor = left_previous.next
            if current_index == right + 1:
                right_next = cursor
            if left <= current_index <= right:
                next_current = cursor.next
                cursor.next = center_link
                center_link = cursor
            else:
                cursor = cursor.next
            current_index += 1
        left_cursor.next = right_next
        if left_previous is None:
            return center_link
        left_previous.next = center_link
        return head

