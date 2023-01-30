#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import OrderedDict


class LFUCache:
    # OrderedDict in python is implemented by a dict+linkedList, which is essentially a LRU cache.
    # "keyfreq" dict represents a normal dict that maps one key to one frequency.
    # "freqkeys" dict represents a dict that maps one freq to many keys, and these "many keys" are stored in OrderedDict.
    # With this two dicts, given one key, we can find its frequency
    # and with its frequency, we can find all other keys of the same frequency.
    # When there are many items of same frequency, 
    # the OrderedDict in freqkeys dict correctly records the item order in LRU Cache fashion 
    # where the first item will be the one to pop out.
    # In the data structure, the minimum frequency is kept track by constant updating
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minfreq = 0
        self.keyfreq = {}
        self.freqkeys = {}
    
    # a function that update the key and frequency hash_tables
    # called from both get and put functions
    def maintenance(self, key):
        freq = self.keyfreq[key] # frequency of the corresponding key
        val = self.freqkeys[freq][key] # the value that we find in the ordered dictionary
        self.freqkeys[freq].pop(key)
        # update minfreq and freqkeys hash table if needed 
        if not self.freqkeys[freq] and freq == self.minfreq: 
            self.minfreq += 1
            self.freqkeys.pop(freq)
        # add to the new frequency
        self.keyfreq[key] = freq + 1
        if freq + 1 not in self.freqkeys:
            self.freqkeys[freq+1] = OrderedDict()
        self.freqkeys[freq + 1][key] = val

    def get(self, key: int) -> int:
        if key not in self.keyfreq:
            return -1
        else:
            self.maintenance(key)
            return self.freqkeys[self.keyfreq[key]][key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        # update the value of key if present
        if key in self.keyfreq:
            freq = self.keyfreq[key]
            self.freqkeys[freq][key] = value            
        else:
            # remove the least recently used, least frequently used value
            if self.capacity == len(self.keyfreq):
                delkey, delval = self.freqkeys[self.minfreq].popitem(last=False)
                self.keyfreq.pop(delkey)

            self.keyfreq[key] = 0
            self.freqkeys[0] = OrderedDict()
            self.freqkeys[0][key] = value
            self.minfreq = 0        
        self.maintenance(key)
                
                
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

