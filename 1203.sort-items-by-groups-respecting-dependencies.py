#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a topological sort problem
    Because group members have to lie next to each other in the sorted list, it suggests we should perform sorting in two different levels
    First we topologically sort individual nodes inside each groups
    For each wild card nodes belonging to -1, we assign new 1 member grop for each wild card nodes
    After all the groups are sorted, we topologically sort the groups
    Any time we detect a cycle, we return []
    '''
    
    def topo_sort(self, all_elements, order):
        G, degree = {}, {}
        for j, k in order:
            if j not in G:
                G[j] = []
            if k not in degree:
                degree[k] = 0
            G[j].append(k)
            degree[k] += 1
        bfs = [j for j in all_elements if j not in degree]
        for j in bfs:
            if j in G:
                for k in G[j]:
                    degree[k] -= 1
                    if degree[k] == 0:
                        bfs.append(k)
        return bfs
    
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Build the groups and the mapping from index to group
        Groups = [[] for i in range(m)]
        indextogroup = [-1]*n
        for i, item in enumerate(group):
            if item == -1:
                Groups.append([i])
                indextogroup[i] = len(Groups) - 1
            else:
                Groups[item].append(i)
                indextogroup[i] = item
        
        # Separate intragroup and intergroups
        intragroup = [[] for i in range(len(Groups))]
        intergroup = []
        for i, item_list in enumerate(beforeItems):
            for beforeitem in item_list:
                if indextogroup[i] == indextogroup[beforeitem]:
                    intragroup[indextogroup[i]].append([beforeitem, i])
                else:
                    intergroup.append([indextogroup[beforeitem], indextogroup[i]])
        
        # Topological sort for each group
        m = len(Groups)
        for i in range(m):
            if intragroup[i]:
                bfs = self.topo_sort(Groups[i], intragroup[i])
                if len(bfs) == len(Groups[i]):
                    Groups[i] = bfs
                else:
                    return []
        
        # Topological sort for different groups
        bfs = self.topo_sort([i for i in range(m)], intergroup)
        result = []
        if len(bfs) == m:  
            for i in bfs:
                result += Groups[i]
        return result 
# @lc code=end

