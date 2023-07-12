#
# @lc app=leetcode id=1806 lang=python3
#
# [1806] Minimum Number of Operations to Reinitialize a Permutation
#

# @lc code=start
class Solution:
    '''
    We can use BFS from each index and find all the possible positions. The result the maximum cluster size
    '''
    def reinitializePermutation(self, n: int) -> int:
        seen = [False] * n
        result = 0
        for i in range(n):
            if not seen[i]:
                dq = deque()
                seen[i] = True
                dq.append(i)
                ans = 0
                while dq:
                    node = dq.popleft()
                    ans += 1
                    nxt = node // 2 if node % 2 == 0 else n // 2 + (node - 1) // 2
                    if not seen[nxt]:
                        seen[nxt] = True
                        dq.append(nxt)
                result = max(result, ans)
        return result
# @lc code=end

