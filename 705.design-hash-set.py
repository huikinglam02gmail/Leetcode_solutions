#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet: 
    '''
    We use multiplicative hashing here. The hash function is h = ((a * K) % W) / (W / M). Here The value a is an appropriately chosen value that should be relatively prime to W. W is the machine word size, and M is the range of resulting has values [0, M - 1]. As there will be at most 10000 calls, taking M as 2 ^ 15 should be good. Here I chose a = 1031231. For W, I chose it to be 2 ^ 20 (no need to be the machine word size). Also we make use of the identity a % (1 << b) = a & ((1 << b) - 1) 
    '''
    
    def eval_hash(self, key):
        return ((key*1031231) & ((1<<20) - 1))>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

