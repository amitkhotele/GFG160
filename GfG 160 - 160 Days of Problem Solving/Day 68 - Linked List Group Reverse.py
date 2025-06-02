class Solution:
    def reverseKGroup(self, head, k):
        if not head or k==1:
            return head

        curr = head
        prev = None
        count = 0

        while curr and count <k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next:
            head.next = self.reverseKGroup(next,k)

        return prev
