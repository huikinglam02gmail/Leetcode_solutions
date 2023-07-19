#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class ListNode:
    def __init__(self, val=[-1, -1], prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.tail = ListNode([-1, -1], None, None)
        self.head = ListNode([-1, -1], None, self.tail)
        self.tail.prev = self.head
        self.count = 0
    
    def append(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.count += 1
    
    def popleft(self):
        deletedKey = self.tail.prev.val[0]
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.count -= 1
        return deletedKey
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1
        return node

    def DoublyLinkedListPrint(self):
        values = []
        temp = self.head
        while temp:
            values.append(temp.val)
            temp = temp.next
        print(values)


class LRUCache:
    '''
    1 <= capacity <= 3000
    So we know we should use a doubly linked list (put and pop O(1) time) together with a hash table (put and get O(1) time) to achieve that 
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = DoublyLinkedList()
        self.hashTable = {}

    def get(self, key: int) -> int:
        if key not in self.hashTable:
            return -1
        else:
            node = self.q.removeNode(self.hashTable[key])
            self.q.append(node)
            return self.hashTable[key].val[1]

    def put(self, key: int, value: int) -> None:
        if key not in self.hashTable:
            if self.q.count == self.capacity:
                self.hashTable.pop(self.q.popleft())            
            node = ListNode([key, value])
            self.hashTable[key] = node
        else:
            node = self.q.removeNode(self.hashTable[key])
            node.val = [key, value]
        self.q.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

