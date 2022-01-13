# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            # current 변수에 현재 head를 담는다.
            current = head
            # head는 맨 앞의 노드를 제거한다
            head = head.next
            # current의 다음 노드로 prev를 이어준다
            current.next = prev
            # prev를 current와 동일하게 변경해준다.
            prev = current
            # none
            # 1 -> none
            # 2 -> 1 -> none
            # ...
            # 5 -> 4 -> 3 -> 2 -> 1
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        while head:
            current = head
            head = head.next
            current.next = temp
            temp = current
        return temp