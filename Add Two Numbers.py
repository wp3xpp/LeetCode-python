##You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
##
##Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
##Output: 7 -> 0 -> 8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        Sum = l1.val + l2.val
        Val = Sum % 10
        Flag = Sum / 10 #进位标志位
        pHead = ListNode(Val)
        pTail = pHead
        l1,l2 = l1.next, l2.next
        while l1 != None and l2 != None:
            Sum = l1.val + l2.val + Flag
            Val = Sum % 10
            pNew = ListNode(Val)
            pTail.next = pNew
            pTail = pNew
            Flag = Sum / 10
            l1,l2 = l1.next, l2.next
        while l1 != None:
            Sum = Flag + l1.val
            Val = Sum % 10
            pNew = ListNode(Val)
            pTail.next = pNew
            pTail = pNew
            Flag = Sum / 10
            l1 = l1.next
        while l2 != None:
            Sum = Flag + l2.val
            Val = Sum % 10 
            pNew = ListNode(Val)
            pTail.next = pNew
            pTail = pNew
            Flag = Sum / 10
            l2 = l2.next
        if l1 == None and l2 == None and Flag:
            pNew = ListNode(1)
            pTail.next = pNew
            pTail = pNew
        return pHead
