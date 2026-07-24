# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        place = 0
        num2=0

        while l1 is not None:
            num1+= l1.val * (10 ** place)
            place += 1
            l1 = l1.next
        place = 0
        
        while l2 is not None:
            num2 += l2.val * (10 ** place)
            place += 1
            l2 = l2.next
        
        num=num1+num2
        dummy = ListNode(0)
        current = dummy
        if(num==0):
            return ListNode(0)


        while num >0:
            digit = num % 10
            current.next = ListNode(digit)  # create new node
            current = current.next          # move forward
            num //= 10
        

        return dummy.next
     

            
            

        