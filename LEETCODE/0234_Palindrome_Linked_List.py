'''
이미 연결 리스트 형태로 구현되어 있는 상태
- 입력값으로 들어 오는 head 예시
    ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
    ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
    ListNode{val: 2, next: ListNode{val: 1, next: None}}
- next가 None이면 ListNode 끝남
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_list = []
        
        node = head
        while node:
            head_list.append(node.val)
            node = node.next
        
        return head_list == head_list[::-1]
