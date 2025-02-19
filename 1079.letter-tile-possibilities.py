#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
class Solution:
    '''
    1 <= tiles.length <= 7 -> brute force seems ok to use
    '''    
    def dfs(self, string, tiles):
        if len(string) > 0: self.word_set.add(string)
        for i in range(len(tiles)):
            self.dfs(string + tiles[i], tiles[:i] + tiles[i+1:])
    
    def numTilePossibilities(self, tiles: str) -> int:
        self.word_set = set()
        self.dfs("", tiles)
        return len(self.word_set)
        
# @lc code=end

