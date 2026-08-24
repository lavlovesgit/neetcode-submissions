# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=1
        cur=head
        while(cur.next is not None):
            cur=cur.next
            l+=1
        index_rem=l-n
        if index_rem == 0:
            return head.next
        cur=head
        c=1




        while(cur.next is not None):
            if(c==(index_rem)):
                cur.next=cur.next.next
                break
            cur=cur.next
            c+=1
            
        return head


        
            
        