#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
import heapq
class Solution:
    '''
    Use a max heap to hold how many a,b and c are left behind
    Add min(count(c), 2) c's to the string
    Update the heap
    If you see the same character as the last inserted, pop a second one and only put in 1 of it    
    '''

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, [- a, 'a'])
        if b > 0:
            heapq.heappush(heap, [- b, 'b'])
        if c > 0:
            heapq.heappush(heap, [- c, 'c'])  
        result = ""
        while heap:
            item, first = heapq.heappop(heap)
            if len(result) > 0 and first == result[-1]:
                if heap:
                    item2, second = heapq.heappop(heap)
                    result += second
                    item2 += 1
                    if item2 != 0: heapq.heappush(heap, [item2, second])
                    heapq.heappush(heap, [item, first])
                else:
                    return result
            else:
                count = min(2, - item)
                result += count * first
                item += count
                if item != 0: heapq.heappush(heap, [item, first])
        return result
# @lc code=end

