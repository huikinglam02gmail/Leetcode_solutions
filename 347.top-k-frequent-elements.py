#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List


class Solution:
    '''
    First use a hash table to store frequency of nums
    Bucket sort: put the keys into len(nums) buckets of size 1
    Then scan the buckets from large to small to give k of them    
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 0
            hash_table[num] += 1
        
        freq = [[] for i in range(len(nums))]
        for key, v in hash_table.items():
            freq[v-1].append(key)
        result = []
        count = 0
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i]) > 0:
                j = 0
                while count < k and j < len(freq[i]):
                    result.append(freq[i][j])
                    j += 1
                    count += 1
        return result
# @lc code=end

