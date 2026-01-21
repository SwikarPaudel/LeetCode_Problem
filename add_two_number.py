# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy 

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next
    
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def main():

    l1_list = [5,4,3]
    l2_list = [2,6,4]

    l1 = build_linked_list(l1_list)
    l2 = build_linked_list(l2_list)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    # Print result linked list
    print("Result:", end=" ")
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

if __name__ == "__main__":
    main()
        