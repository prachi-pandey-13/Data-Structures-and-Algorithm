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
        # length = 0
        # temp = head
        # while temp is not None:
        #     length += 1
        #     temp = temp.next
        # if length == n:
        #     newhead = head.next
        #     del head
        #     return newhead
        # pos_to_stop = length - n
        # temp = head
        # count = 1
        # while count < pos_to_stop:
        #     temp = temp.next
        #     count += 1
        # temp.next = temp.next.next
        # return head

        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head