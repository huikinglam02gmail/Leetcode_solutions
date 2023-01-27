#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
from typing import List

class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True


class Solution:
    # Alternative solution: same logic, but use Trie to save memory
    # We first record each word into the wordSet Trie
    # Then for each word, we traverse through the wordSet Trie
    # Whenever we reach word end and can find another children, we repeat the traversal starting from root
    # If failed, we write the word into the failed Trie 

    def dfs(self, node, word, count):
        if len(word) == 0:
            return count > 1
        i = 0
        while i < len(word) and word[i] in node.children:
            node = node.children[word[i]]
            if node.isEnd and self.dfs(self.wordSet.root, word[i+1:], count + 1):
                return True
            i += 1
        return False
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.wordSet, result = Trie(), []
        for word in words:
            self.wordSet.insert(word)

        for word in words:
            if self.dfs(self.wordSet.root, word, 0):
                result.append(word)
        return result


# @lc code=end

