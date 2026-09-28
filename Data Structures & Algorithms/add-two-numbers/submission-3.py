# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val//10
            val = val%10
            cur.next = ListNode(val)  #create new node

            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


        #traverse to end then go bac
        # my_list = ListNode()
        # list1 = []
        # list2 = []
        # while l1 is not None:
        #     list1.append(l1.val)
        #     l1 = l1.next
            
        # while l2 is not None: 
        #     list2.append(l2.val)
        #     l2 = l2.next
        # # list1.reverse()
        # # list2.reverse()
        # final = []
        # add = 0
        # for i in range(min(len(list1),len(list2))):
        #     if list1[i]+list2[i]+add < 10:
        #         final.append(list1[i]+list2[i]+add)
        #         add = 0
        #     else:
        #         final.append(list1[i]+list2[i]+add-10)
        #         add = 1
        # longer = max(len(list1), len(list2))
        # longer_index = len(longer)-min(len(list1),len(list2))
        # for i in range(longer_index):
        #     if longer[i] + add >= 10:
        #         final.append(longer[i] + add -10)
        #         add = 1
        #     else:
        #         final.append(longer[i]+add)
        #         add = 0
        # if add > 0:
        #     final.append(1)
        

        # dummy = ListNode()
        # curr = dummy
        # for i in final:
        #     curr.next = ListNode(i)
        #     curr = curr.next
        # return dummy.next

    


        
        # return 


        
        