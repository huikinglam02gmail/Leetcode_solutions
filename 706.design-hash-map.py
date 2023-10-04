#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:
    '''
    Multiplicative hashing: a K MOD 2 ^ w / 2 ^ (w - m): a is relatively prime to 2 ^ w: we choose a = 1031231, w = 20 and m = 15 and I choose w = 20. m is chosen such that 1 << m > number of operation (potential collisions). Also we use the trick: for any s: s % (2^t) = s & (1<<t) - 1
    '''
    def eval_hash(self, key):
        return ((key * 1031231) & (1<<20) - 1) >> 5

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]
        
    def put(self, key, value):
        t = self.eval_hash(key)
        for i,(k, v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t][i] = (k, value)
                return
        self.arr[t].append((key, value))

    def get(self, key):
        t = self.eval_hash(key)
        for i,(k, v) in enumerate(self.arr[t]):
            if k == key: 
                return v
        return -1

    def remove(self, key: int):
        t = self.eval_hash(key)
        for i,(k, v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t].remove((k,v))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

