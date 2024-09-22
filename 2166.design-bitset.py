#
# @lc app=leetcode id=2166 lang=python3
#
# [2166] Design Bitset
#

# @lc code=start
class Bitset:
    '''
    At most 5 calls will be made to toString.
    So we can keep flipCount[i] = number of flips at ith bit
    '''
    def __init__(self, size: int):
        self.flipCount = [0] * size
        self.size =  size
        self.totalOne = 0
        self.totalFlip = 0

    def fix(self, idx: int) -> None:
        if (self.flipCount[idx] + self.totalFlip) % 2 == 0:
            self.totalOne += 1
            self.flipCount[idx] += 1

    def unfix(self, idx: int) -> None:
        if (self.flipCount[idx] + self.totalFlip) % 2 == 1:
            self.totalOne -= 1
            self.flipCount[idx] += 1
        
    def flip(self) -> None:
        self.totalFlip += 1
        self.totalOne =  self.size - self.totalOne

    def all(self) -> bool:
        return self.totalOne == self.size

    def one(self) -> bool:
        return self.totalOne > 0

    def count(self) -> int:
        return self.totalOne

    def toString(self) -> str:
        return "".join([str((count + self.totalFlip) % 2) for count in self.flipCount])
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
# @lc code=end

