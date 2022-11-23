#
# @lc app=leetcode id=1488 lang=python3
#
# [1488] Avoid Flood in The City
#

# @lc code=start
import bisect
import heapq


class Solution:
    # The problem can be solved using a hash table and a priority queue
    # First we pass through rains and record when it rains on each lake
    # In the second pass, we keep a priority queue of next rain date
    # When we see rain, we first check if the rains[i] is already full.
    # If so, return []
    # If not, we add rains[i] to the full list. 
    # If there is a next rain in rains[i] at time j, add [j, rains[i]] to the priority queue
    # return -1
    # The critical part is when rains[i] = 0
    # There we will choose the lake which the next rain is soonest, 
    # We empty it and remove from full

    def avoidFlood(self, rains: List[int]) -> List[int]:
        Record = {}
        for i, rain in enumerate(rains):
            if rain not in Record:
                Record[rain] = []
            Record[rain].append(i)
        coming = []
        full = set()
        result = []
        for i, rain in enumerate(rains):
            if rain > 0:
                if rain in full:
                    return []
                else:
                    full.add(rain)
                    ind = bisect.bisect_right(Record[rain], i)
                    if ind < len(Record[rain]):
                        heapq.heappush(coming, [Record[rain][ind], rain])
                    result.append(-1)
            else:
                if coming:
                    ind, lake = heapq.heappop(coming)
                    full.remove(lake)
                    result.append(lake)
                else:
                    result.append(1)
        return result


# @lc code=end

