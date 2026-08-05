# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

        # temp = head
        # n = 0
        # while temp is not None:
        #     n += 1
        #     temp = temp.next
        # temp = head
        # for i in range(0, n//2):
        #     temp = temp.next
        # return temp