/*
 * @lc app=leetcode id=208 lang=csharp
 *
 * [208] Implement Trie (Prefix Tree)
 */

// @lc code=start
using System.Collections.Generic;
public class TrieNode
{
    public Dictionary<char, TrieNode> children;
    public bool isEnd;
    public TrieNode()
    {
        children = new Dictionary<char, TrieNode>();
        isEnd = false;
    }
}
public class Trie 
{
    TrieNode root;
    public Trie() 
    {
        root = new TrieNode();
    }
    
    public void Insert(string word) 
    {
        TrieNode node = root;
        foreach (char c in word)
        {
            if (!node.children.ContainsKey(c))
            {
                node.children[c] = new TrieNode();
            }
            node = node.children[c];
        }    
        node.isEnd = true;
    }
    
    public bool Search(string word) 
    {
        TrieNode node = root;
        foreach (char c in word)
        {
            if (!node.children.ContainsKey(c))
            {
                return false;
            }
            node = node.children[c];
        }    
        return node.isEnd;
    }
    
    public bool StartsWith(string prefix) 
    {    
        TrieNode node = root;
        foreach (char c in prefix)
        {
            if (!node.children.ContainsKey(c))
            {
                return false;
            }
            node = node.children[c];
        }    
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */
// @lc code=end

