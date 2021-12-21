class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 임의로 listNode 담을 변수, 현재 위치 표시하는 변수
        temp = current = ListNode(0)
        #만약 list1과 list2가 모두 존재할 때
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        # 만약 둘 중 하나라도 존재한다면, 현재 노드의 next가 됨. (current는 오름차순 노드 리스트니까)  
        current.next = list1 or list2
        #처음에 0으로 시작한 첫 값 제외하고, temp.next를 리턴
        return temp.next