#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#

# @lc code=start
class Solution:
    '''
    use a hash_table to store the indices of characters inside the ring           
    Use a list to store the minimum steps to finish typing the current key
    Enumerate minimum of all possible steps from different starts to a certain spot
    to go from index i to j, minimum step = min(abs(i - j), l_r - abs) 
    '''
    def findRotateSteps(self, ring: str, key: str) -> int:
        hash_ring = [[] for i in range(26)]
        for i, c in enumerate(ring): hash_ring[ord(c) - ord('a')] .append(i)
        l_r = len(ring)

        steps = [[float('inf') for j in range(l_r)] for i in range(len(key))]
        starts = [0]
        for i, c in enumerate(key):
            ends = hash_ring[ord(c) - ord('a')]
            for end in ends:
                for start in starts:
                    if i == 0:
                        steps[i][end] = min(steps[i][end],  1 + abs(start - end), 1 + l_r - abs(start - end))
                    else:
                        steps[i][end] = min(steps[i][end],  steps[i - 1][start] + 1 + abs(start - end), steps[i - 1][start] + 1 + l_r - abs(start - end))
            starts = ends
        return min(steps[len(key) - 1][:])
# @lc code=end

