#
# @lc app=leetcode id=1733 lang=python3
#
# [1733] Minimum Number of People to Teach
#

# @lc code=start
from typing import List


class Solution:
    '''
    Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z. This means graph is not appropriate for the problem. Instead we should consider between each pair of friend, which language does not intersect. Since 2 <= n <= 500 and 1 <= friendships.length <= 500, we can test for each language how many user we need to teach and get the minimum.
    '''
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang = [set(l) for l in languages]
        frds = [f for f in friendships if len(lang[f[0] - 1].intersection(lang[f[1] - 1])) == 0]
        result = float('inf')
        for i in range(1, n + 1):
            teach = set()
            for u, v in frds:
                if i not in lang[u - 1]:
                    teach.add(u)
                if i not in lang[v - 1]:
                    teach.add(v)
            result = min(result, len(teach)) 
        return result              
# @lc code=end
