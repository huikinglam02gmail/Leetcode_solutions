#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        pCrawl = self.root
        for c in word:
            if c not in pCrawl.children:
                pCrawl.children[c] = TrieNode()
            pCrawl = pCrawl.children[c]
        pCrawl.isEnd = True        

    def search(self, word: str) -> bool:
        pCrawl = self.root
        for c in word:
            if c not in pCrawl.children:
                return False
            pCrawl = pCrawl.children[c]
        return pCrawl.isEnd

    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root
        for c in prefix:
            if c not in pCrawl.children:
                return False
            pCrawl = pCrawl.children[c] 
        return True       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

