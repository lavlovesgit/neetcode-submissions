# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1=head
        fast=head
        slow=head
        while(fast is not None and fast.next is not None and fast.next.next is not None):
            fast=fast.next.next
            slow=slow.next
        head2=slow.next
        slow.next=None
        #reversing the other half

        prev,cur=None,head2
        while(cur is not None):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp  

        list2=prev 

        dummy=ListNode()
        tail=dummy   

        while list1 and list2: 
            tail.next=list1
            list1=list1.next 
            tail=tail.next

            tail.next=list2
            list2=list2.next 
            tail=tail.next

        if list1:
            tail.next=list1
        else:
            tail.next=list2
        
        