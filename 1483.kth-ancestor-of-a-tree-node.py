#
# @lc app=leetcode id=1483 lang=python3
#
# [1483] Kth Ancestor of a Tree Node
#

# @lc code=start
class TreeAncestor:
    # If we track every parent of every node, the preparation time and memory needed would be O(n^2), which is too long
    # On the other hand, we can prepare the parent graph such that each query will only take log(k) time
    # To do that, we can instead save the 2^j th parent of each node
    # dp[i][j] = 2^j parent of node i
    # We first go through the parent array and record dp[i][0]
    # Then we scan for j = 1: if dp[i][j-1] = dp[i][0] != -1, the corresponding node is parent's parent of the current node
    # Repeat the process until j = 16 (2^16 = 65536 > n)
    # Then for each query, we decompose k into powers of 2 (binary representation)
    # For example, if k = 5, the binary representation is 101
    # We first start from node, look up what dp[node][0] is because the 0th digit is 1
    # Then we change to node to dp[i][0]. The next digit is 0, no need to do anything
    # Then we return dp[dp[node][0]][2]

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1 for i in range(16)] for j in range(n)]
        for ch, pa in enumerate(parent):
            self.dp[ch][0] = pa
        for j in range(1, 16):
            for i in range(n):
                if self.dp[i][j-1] >= 0:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
        
    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k > 0 and node >= 0:
            if (k&(1 << i)) != 0:
                node = self.dp[node][i]
                k ^= (1 << i)
            i += 1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end

