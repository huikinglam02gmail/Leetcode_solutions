#
# @lc app=leetcode id=2182 lang=python3
#
# [2182] Construct String With Repeat Limit
#

# @lc code=start
import heapq


class Solution:
    '''
    Count what's remaining and keep a heap to hold next available character
    '''
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = [0] * 26
        for c in s: counts[ord(c) - ord('a')] += 1
        heap = []
        for i in range(26): 
            if counts[i] > 0: heapq.heappush(heap, [- i, counts[i]])
        result = []
        repeats = 0
        while heap:
            negOrd1, avail1 = heapq.heappop(heap)
            if heap and result and ord('a') - ord(result[-1]) == negOrd1 and repeats == repeatLimit:
                negOrd2, avail2 = heapq.heappop(heap)
                result.append(chr(ord('a') - negOrd2))
                avail2 -= 1
                repeats = 1
                heapq.heappush(heap, [negOrd1, avail1])
                if avail2 > 0: heapq.heappush(heap, [negOrd2, avail2])
            elif (result and ord('a') - ord(result[-1]) != negOrd1) or repeats < repeatLimit:
                repeats = repeats + 1 if result and (ord('a') - ord(result[-1]) == negOrd1) else 1
                result.append(chr(ord('a') - negOrd1))
                avail1 -= 1
                if avail1 > 0: heapq.heappush(heap, [negOrd1, avail1])                             
        return "".join(result)

            
        
# @lc code=end

