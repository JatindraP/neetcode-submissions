# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divideMarge(lists)
    def divideMarge(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        m = len(lists)//2
        l1=self.divideMarge(lists[:m])
        l2=self.divideMarge(lists[m:])
        s_list = self.merge(l1,l2)
        return s_list

    def merge(self,l1:ListNode,l2:ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next= l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return head.next


        