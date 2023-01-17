#
# @lc app=leetcode id=1622 lang=python3
#
# [1622] Fancy Sequence
#

# @lc code=start
class Fancy:
    # The final number at all index = a*x + b
    # So for each appended number, we restore it back to as if it is present in the first number
    # x = (val - b) * modinv(a) 
    # for each add, we add to b
    # for each mult, we multiply a and b both by item

    def __init__(self):
        self.result = []
        self.a = 1
        self.b = 0
        self.MOD = pow(10, 9) + 7

    def append(self, val: int) -> None:
        self.result.append( (pow(self.a, -1, self.MOD) * ((val - self.b + self.MOD) % self.MOD)) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.b += inc
        self.b %= self.MOD

    def multAll(self, m: int) -> None:
        self.a *= m
        self.a %= self.MOD
        self.b *= m
        self.b %= self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.result):
            return -1
        else:
            return (((self.a % self.MOD) * (self.result[idx] % self.MOD)) % self.MOD + self.b) % self.MOD
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# @lc code=end

