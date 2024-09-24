#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
from typing import List

class TrieNode:
    def __init__(self, characterCount) -> None:
        self.children = [None for i in range(characterCount)]
        self.wordEnd = False

class Trie:
    def __init__(self, characterCount):
        self.root = TrieNode(characterCount)
        self.characterCount = characterCount
    
    def insert(self, word, baseCharacter):
        temp = self.root
        for c in word:
            if not temp.children[ord(c) - ord(baseCharacter)]: temp.children[ord(c) - ord(baseCharacter)] = TrieNode(self.characterCount)
            temp = temp.children[ord(c) - ord(baseCharacter)]
        temp.wordEnd = True
    
    def search(self, word, baseCharacter):
        temp = self.root
        level = 0
        for c in word:
            if not temp.children[ord(c) - ord(baseCharacter)]: return [level, False]
            temp = temp.children[ord(c) - ord(baseCharacter)]
            level += 1
        return [level, temp.wordEnd]

class Solution:
    '''
    1 <= arr1[i], arr2[i] <= 10^8, At most 8 layers of Trie
    So form a Trie with numbers from arr1. Then track deepest level each num in arr2 can Trie traversal reach.
    '''
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie(10)
        for num in arr1: trie.insert(str(num), '0')
        result = 0
        for num in arr2:
            l, isEnd = trie.search(str(num), '0')
            result = max(result, l)
        return result

# @lc code=end

