#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from typing import List


class TrieNode(object):
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    '''
    Build a Trie to store all the roots in dictionary
    Then for each word in sentence, look for first ending root in the Trie and add it    
    '''
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isEnd = True
        
        sentence_split = sentence.split(' ')
        result = []
        for word in sentence_split:
            node = root
            string = ""
            for c in word:
                if c not in node.children:
                    string = word
                    break
                else:
                    node = node.children[c]
                    string += c
                    if node.isEnd: break
            result.append(string)
        return " ".join(result)
# @lc code=end

