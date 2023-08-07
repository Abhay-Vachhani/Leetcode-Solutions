from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList = ListNode()
        listHead = newList

        while True:
            if list1 != None and list2 != None and list1.val < list2.val:
                newList.next = ListNode()
                newList = newList.next
                newList.val = list1.val
                list1 = list1.next
            else:
                if list1 != None and list2 == None:
                    newList.next = ListNode()
                    newList = newList.next
                    newList.val = list1.val
                    list1 = list1.next

                if list2 != None:
                    newList.next = ListNode()
                    newList = newList.next
                    newList.val = list2.val
                    list2 = list2.next

            if list1 == None and list2 == None:
                break
        return listHead.next


# Input Testing
def list2listNode(lst):
    list1 = ListNode()
    tmp = list1

    for i in lst:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return list1.next


def getOutput(list1, list2):
    lst = Solution().mergeTwoLists(
        list1=list2listNode(list1), list2=list2listNode(list2)
    )

    while lst != None:
        print(lst.val, end=", ")
        lst = lst.next
    print()


getOutput([1, 2, 4], [1, 3, 4])
getOutput([], [])
getOutput([], [0])
