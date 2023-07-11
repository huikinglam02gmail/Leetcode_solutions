#
# @lc app=leetcode id=1803 lang=python3
#
# [1803] Count Pairs With XOR in a Range
#

# @lc code=start
class TrieNode():
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Trie():
    def __init__(self, levels):
        self.root = TrieNode()
        self.levels = levels

    def countXORPairsSmallerThanK(self, num, k):
        node = self.root
        result = 0
        level = self.levels - 1
        while node != None and level >= 0:
            ind =  ((k ^ num) & (1 << level)) // (1 << level)
            if (k & (1 << level)) > 0 and node.children[1 - ind]:
                result += node.children[1 - ind].count
            node = node.children[ind]
            level -= 1
        return result
    
    def addNewNumber(self, num):
        node = self.root
        for i in range(self.levels - 1, -1, -1):
            digit = (num & (1 << i)) // (1 << i)
            if not node.children[digit]:
                node.children[digit] = TrieNode()
            node = node.children[digit]
            node.count += 1

class Solution:
    '''
    The problem can be broken down into (# of pairs with XOR < high + 1) - (# of pairs with XOR < low)
    To find # of pairs with XOR < k, we can represent num as binary representation: 1 <= nums[i] <= 2 * 10^4, so binary string of 15 bits is enough
    (in principle we only need up max(max(nums), high + 1))
    For each number num, we first break it down into its binary representation. Like in example 2, suppose we have seen 9 = "1001" and we have 8 = "1000"
    For k = 15 = "1111". To check if we have number with num ^ 8 < 15 inside the Trie, we know any existing number with 0th digit = 1 must be valid, because "1XXX" ^ "1000" = "0???", which is smaller than "1111". Then we go down 1 level along all numbers with 0th digit = 0. Conversely, if we have 5 ("0101") instead of 8, any existing number with 0th digit = 0 will be valid. Then we go down 1 level along with all number with 0th digit = 1
    '''
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie =  Trie(max(max(nums), high + 1).bit_length())
        result = [0, 0]
        limit = [low, high + 1]
        for num in nums:
            for j in range(2):
                result[j] += trie.countXORPairsSmallerThanK(num, limit[j])
            trie.addNewNumber(num)
        return result[1] - result[0]
# @lc code=end

