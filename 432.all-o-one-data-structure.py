#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start        
class Node:
    def __init__(self, key, count, prev, next):
        self.key = key
        self.count = count
        self.prev = prev
        self.next = next
        
class AllOne:
    '''
    Use a hash table using the given strings as keys. The value would point to a doubly linked list node, with values sorted from low to high. Also, the node should store the string key for easy reference
    Increment and decrement are equivalent to swapping nodes between neighbours, therefore O(1)
    get MaxKey and getMinKey would be equivalent to getting the head and end of the doubly linked list    
    '''
    def __init__(self):
        self.hash_table = {}
        self.head = Node("HEAD", -1, None, None)
        self.tail = Node("TAIL", 50001, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def switch(self, node1, node2):
        if node2.next:
            node1.next = node2.next
            node1.next.prev = node1
        else:
            node1.next = None
            
        if node1.prev:
            node1.prev.next = node2
            node2.prev = node1.prev
        else:
            node2.prev = None

        node2.next = node1
        node1.prev = node2

    
    def inc(self, key: str) -> None:
        if key not in self.hash_table:
            self.hash_table[key] = Node(key, 1, None, self.head)
            self.head.prev = self.hash_table[key]
            temp1 = self.hash_table[key]
            temp2 = self.head
        else:
            self.hash_table[key].count += 1
            temp1 = self.hash_table[key]
            temp2 = self.hash_table[key].next
        while temp1.count > temp2.count:
            self.switch(temp1, temp2)
            temp1, temp2 = temp2.next, temp1.next

    def dec(self, key: str) -> None:
        if key not in self.hash_table:
            return
        else:
            self.hash_table[key].count -= 1
            if self.hash_table[key].count == 0:
                self.hash_table[key].next.prev = self.hash_table[key].prev
                self.hash_table[key].prev.next = self.hash_table[key].next
                self.hash_table.pop(key)
            else:
                temp1 = self.hash_table[key].prev
                temp2 = self.hash_table[key]
                while temp1.count > temp2.count:
                    self.switch(temp1, temp2)
                    temp1, temp2 = temp2.prev, temp1.prev

    def getMaxKey(self) -> str:
        if self.tail.prev.key == "HEAD":
            return ""
        else:
            return self.tail.prev.key
        
    def getMinKey(self) -> str:
        if self.head.next.key == "TAIL":
            return ""
        else:
            return self.head.next.key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

