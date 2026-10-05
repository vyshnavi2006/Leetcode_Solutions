# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        self.prev = None
        self.current = head
        while(self.current!=None):
            self.next = self.current.next
            self.current.next = self.prev
            self.prev = self.current
            self.current = self.next
        return self.prev