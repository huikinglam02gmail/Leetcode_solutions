#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    '''
    We could build a Trie to solve this problem
    First we sort folder lexicographically
    Then we try to propel each word through the Trie
    At each step, we check if we are at the end of a word. If so, we abort action
    Otherwise we build new nodes or follow the old nodes and keep on searching
    When we reach the end of word, we add a new word to the Trie and to the result    
    '''
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        root, result = TrieNode(), []
        for word in folder:
            node = root
            word_split = word.split("/")
            i, n = 1, len(word_split)
            while not node.isEnd and i < n:
                if word_split[i] not in node.children: node.children[word_split[i]] = TrieNode()
                node = node.children[word_split[i]]
                i += 1
            if i == n:
                node.isEnd = True
                result.append(word)
        return result
# @lc code=end

