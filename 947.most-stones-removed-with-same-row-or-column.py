#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
class Solution:
    # This is a BFS problem (or Union find if you wish)
    # The number of stones that can be removed to sum(size of connected components - 1)
    # Build the graph by keeping the x and y coordinates as key, stone index and value
    # Then for each key, BFS from it if it is not yet visited, find the size of connected components
    def removeStones(self, stones: List[List[int]]) -> int:
        hash_table = [{} for i in range(2)]
        n = len(stones)
        for i, stone in enumerate(stones):
            if stone[0] not in hash_table[0]:
                hash_table[0][stone[0]] = []
            hash_table[0][stone[0]].append(i)
            if stone[1] not in hash_table[1]:
                hash_table[1][stone[1]] = []
            hash_table[1][stone[1]].append(i)
        #print(hash_table)
        
        # Build the graph:
        graph = [set() for i in range(n)]
        for x in range(2):
            for key in hash_table[x]:
                for i in range(len(hash_table[x][key])-1):
                    for j in range(i+1, len(hash_table[x][key])):
                        graph[hash_table[x][key][i]].add(hash_table[x][key][j])
                        graph[hash_table[x][key][j]].add(hash_table[x][key][i])
        
        # BFS
        result, visited = 0, set()
        for i in range(n):
            if i not in visited:
                dq, seen = deque(), set()
                dq.append(i)
                seen.add(i)
                visited.add(i)
                while dq:
                    node = dq.popleft()
                    for j in graph[node]:
                        if j not in visited:
                            dq.append(j)
                            seen.add(j)
                            visited.add(j)
                result += len(seen) - 1
        return result
# @lc code=end

