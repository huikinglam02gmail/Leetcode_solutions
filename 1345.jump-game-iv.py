#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    A graph problem. First build the graph, use index to identify nodes, link up the neighbour nodes. At the same time, record the values in a hash table. Then just BFS. There could be a lot of duplicates in the array. To avoid getting into an O(N^2) scenario, we keep track of what value has already been searched. I used an extra visited_values to ensure the loop through the index list will only occur once      
    '''
    def minJumps(self, arr: List[int]) -> int:
        n, hash_table = len(arr), {}
        for i, num in enumerate(arr):
            if num not in hash_table:
                hash_table[num] = []
            hash_table[num].append(i)
        
        dq, visited, visited_values, steps = deque(), [False]*n, set(), 0
        dq.append(0)
        visited[0] = True
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node == n-1:
                    return steps                
                if arr[node] not in visited_values:
                    for nxt in hash_table[arr[node]]:
                        if not visited[nxt]:
                            dq.append(nxt)
                            visited[nxt] = True
                    visited_values.add(arr[node])
                if node > 0 and not visited[node-1]:
                    dq.append(node-1)
                    visited[node-1] = True
                if not visited[node+1]:
                    dq.append(node+1)
                    visited[node+1] = True
            steps += 1
        return -1
# @lc code=end

