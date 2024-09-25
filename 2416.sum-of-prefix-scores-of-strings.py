#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#

# @lc code=start
from typing import List


class TrieNode():
    def __init__(self):
        self.children = {}
        self.passage = 0
        
class Solution:
    '''
    It's asking for prefix of words -> Trie should come to mind immediately
    Build the Trie first, in TrieNodes apart from the root, record how many times words are directed to the node
    Then just go through all the words again and add up the counts in different nodes    
    '''
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        for word in words:
            node = root
            for c in word:
                if c not in node.children: node.children[c] = TrieNode()
                node = node.children[c]
                node.passage += 1
        
        result = []
        for word in words:
            count, node = 0, root
            for c in word:
                node = node.children[c]
                count += node.passage
            result.append(count)
        return result
# @lc code=end

