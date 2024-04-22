#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    As hinted, this is an undirected graph BFS problem
    Treat each status as a node
    Graph connection: at each index, it can be arrive at the adjacent integer at each digit
    "0000" to "0001", "0009", "0010","0090",.. etc
    Therefore the problem is just asking for reachability    
    '''
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        # BFS from "0000"
        dq = deque()
        visited = set()
        steps = 0
        dq.append("0000")
        visited.add("0000")
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node == target: return steps
                if node in deadends: continue
                for j in range(4):
                    if node[j] == "0":
                        node_up = node[:j] + "1" + node[j+1:]
                        node_down = node[:j] + "9" + node[j+1:]
                    elif node[j] == "9":
                        node_up = node[:j] + "0" + node[j+1:]
                        node_down = node[:j] + "8" + node[j+1:]
                    else:
                        node_up = node[:j] + str(int(node[j]) + 1) + node[j+1:]
                        node_down = node[:j] + str(int(node[j]) - 1) + node[j+1:]
                    if node_up not in visited:
                        dq.append(node_up)
                        visited.add(node_up)
                    if node_down not in visited:
                        dq.append(node_down)
                        visited.add(node_down)                        
            steps += 1
        return -1
# @lc code=end

