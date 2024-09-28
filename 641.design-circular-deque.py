#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
# Definition for a doubly_linked_list Node.
class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next
class MyCircularDeque:
    '''
    Similar to Leetcode 622. Only difference is insertion and deletion can happen on both sides    
    '''
    def __init__(self, k: int):
        self.head = self.tail = ListNode(-1,None,None)
        temp = self.head
        for i in range(k-1):
            temp.next = ListNode(-1,None,None)
            temp.next.prev = temp
            temp = temp.next
        temp.next = self.head
        self.head.prev = temp

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.head.prev.val = value
            self.head = self.head.prev
            return True       

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.tail.val = value
            self.tail = self.tail.next
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head.val = -1
            self.head = self.head.next
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.tail.prev.val = -1
            self.tail = self.tail.prev
            return True       

    def getFront(self) -> int:
        return self.head.val

    def getRear(self) -> int:
        return self.tail.prev.val        

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.head.val == -1
    
    def isFull(self) -> bool:
        return self.head == self.tail and self.head.val >= 0        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

