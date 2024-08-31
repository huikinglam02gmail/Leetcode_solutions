#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    This is a topological sort problem.
    Basically we treat each recipes[i] and ingredients[i][j] as nodes
    Then we build the graph: graph[ingredient[i][j]].add(recipes[i]), while counting adjacency of each node.
    Finally we BFS from all nodes of supplies and include all eentries in recipes if it can be reached.
    '''
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipeSet = set(recipes)
        materials = {}
        n = len(recipes)
        adjacencies =  {}
        for i in range(n):
            if recipes[i] not in materials: materials[recipes[i]] = set()
            if recipes[i] not in adjacencies: adjacencies[recipes[i]] = 0
            for ingredient in ingredients[i]:
                if ingredient not in materials: materials[ingredient] = set()
                materials[ingredient].add(recipes[i])
                adjacencies[recipes[i]] += 1
        
        dq = deque()
        for supply in supplies: dq.append(supply)
        result = []
        while dq:
            node = dq.popleft()
            if node in recipeSet: result.append(node)
            if node not in materials: continue
            for nxt in materials[node]:
                adjacencies[nxt] -= 1
                if adjacencies[nxt] == 0: dq.append(nxt)
        return result

# @lc code=end

