#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

class TrieNode(object):    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
        
    def search(self, word):	
        return self.dfs(word, self.root)

    def dfs(self, word, node):
        if len(word) == 0:
            return node.isEnd
        elif word[0] == ".":
            for c in node.children:
                if self.dfs(word[1:], node.children[c]):
                    return True
            return False
        elif word[0] in node.children:
            return self.dfs(word[1:], node.children[word[0]])
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)