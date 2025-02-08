#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#

# @lc code=start
import heapq


class NumberContainers:
    '''
    Use a hash table to map indices to numbers
    Use a hash table of min heap to collect all the indices for a given number
    We use a lazy approach to update the heap    
    '''
    def __init__(self):
        self.indices_to_numbers = {}
        self.numbers_to_indices = {}

    def change(self, index: int, number: int) -> None:
        self.indices_to_numbers[index] = number
        if number not in self.numbers_to_indices: self.numbers_to_indices[number] = []
        heapq.heappush(self.numbers_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.numbers_to_indices: return -1
        while len(self.numbers_to_indices[number]) > 0:
            index = self.numbers_to_indices[number][0]
            if self.indices_to_numbers[index] == number: return index
            heapq.heappop(self.numbers_to_indices[number])
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

