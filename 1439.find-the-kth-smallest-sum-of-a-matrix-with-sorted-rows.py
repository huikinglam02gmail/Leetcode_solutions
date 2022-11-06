#
# @lc app=leetcode id=1439 lang=python3
#
# [1439] Find the Kth Smallest Sum of a Matrix With Sorted Rows
#

# @lc code=start
import heapq


class Solution:
    # k is rather small (<= 200)
    # Therefore we can refer to the solution given in Leetcode 373
    # Key idea: because all the elements contribute to the final sum, the min sum list of mat[:i+1] = min sum combinations between combinations of mat[:i] and mat[i]
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap, n1, n2, visited = [], len(nums1), len(nums2), set()
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
            result.append(nums1[i] + nums2[j])
        return result
    
    
    
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        pairs = mat[0]
        for i in range(m-1):
            pairs = self.kSmallestPairs(pairs, mat[i+1], 200)
        return pairs[k-1]
        
# @lc code=end

