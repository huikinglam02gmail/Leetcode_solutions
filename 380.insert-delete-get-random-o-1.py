#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:
    # keep a hash table and an array to keep the element and index
    # Because all numbers inside the collection are unique by requirement
    # When we remove, we just pop the last element
    # Exchange the value with where holds val

    def __init__(self):    
        self.hash_table = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        result = val not in self.hash_table
        if result:
            self.arr.append(val)
            self.hash_table[val] = len(self.arr)-1
        return result

    def remove(self, val: int) -> bool:
        result = val in self.hash_table
        if result:
            x = self.arr.pop()
            if x != val:
                self.arr[self.hash_table[val]] = x
                self.hash_table[x] = self.hash_table[val]
            self.hash_table.pop(val)
        return result

    def getRandom(self) -> int:
        return self.arr[random.randrange(0,len(self.arr))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

