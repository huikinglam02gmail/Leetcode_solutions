#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
import bisect
from operator import itemgetter


class SnapshotArray:
    '''
    Since we are asked to report the historical values, we should use a hash table to keep the past values
    To initialize, We keep an array of length length, which holds an array of two values: [snap_id, new_value]
    When the get function is called, we binary search on the array[index] for snap_id    
    '''

    def __init__(self, length: int):
        self.history = [[[-1,0]] for i in range(length)]
        self.snap_count = -1

    def set(self, index: int, val: int) -> None:
        last_snap_id = self.history[index][-1][0]
        if last_snap_id == self.snap_count:
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count

    def get(self, index: int, snap_id: int) -> int:
        result = bisect.bisect_right(self.history[index], snap_id-1, key=itemgetter(0))
        return self.history[index][result-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

