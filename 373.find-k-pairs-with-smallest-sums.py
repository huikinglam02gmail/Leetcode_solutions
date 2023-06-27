#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    nums1 and nums2 are both sorted. We therefore maintain a priority queue, putting in the sum of first elements and the indices. Each time we pop, we get the two indices (i, j) and put in nums1[i + 1] + nums2[j] and nums1[i] + nums2[j + 1], if either of them are not visited.
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap, n1, n2 = [], len(nums1), len(nums2)
        visited = set()
        heap.append([nums1[0] + nums2[0], 0, 0])
        visited.add((0,0))

        result = []
        while heap and len(result) < k:
            total, i, j = heapq.heappop(heap)
            if i < n1-1 and (i+1, j) not in visited:
                heapq.heappush(heap, [total - nums1[i] + nums1[i+1], i+1, j])
                visited.add((i+1,j))
            if j < n2-1 and (i, j+1) not in visited:
                heapq.heappush(heap, [total - nums2[j] + nums2[j+1], i, j+1])
                visited.add((i,j+1))
            result.append([nums1[i], nums2[j]])
        return result            
# @lc code=end

