# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow linked list moves 1 at once, fast moves 2
        slow = fast = head
        # check if next of fast link is not None
        while fast and fast.next is not None:
            # slow moves only the half of the list
            slow = slow.next
            fast = fast.next.next
        return slow



# Each time, slow go 1 steps while fast go 2 steps.
# When fast arrives at the end, slow will arrive right in the middle.
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# https://leetcode.com/problems/middle-of-the-linked-list/discuss/154619/C%2B%2BJavaPython-Slow-and-Fast-Pointers



# python linked list example: [파이썬으로 구현하는 링크드 리스트](https://velog.io/@woga1999/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EB%A7%81%ED%81%AC%EB%93%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8)