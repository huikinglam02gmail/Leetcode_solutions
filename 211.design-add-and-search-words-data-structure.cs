/*
 * @lc app=leetcode id=211 lang=csharp
 *
 * [211] Design Add and Search Words Data Structure
 */

// @lc code=start
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
public class WordDictionary 
{
    TrieNode root;
    public WordDictionary() 
    {
        root = new TrieNode();
    }
    
    public void AddWord(string word) 
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
        return dfs(word, root);
    }

    public bool dfs(string word, TrieNode node)
    {
        if (word.Length == 0)
        {
            return node.isEnd;
        }
        else if (word[0] == '.')
        {
            foreach (char c in node.children.Keys)
            {
                if (dfs(word.Substring(1), node.children[c]))
                {
                    return true;
                }
            }
            return false;
        }
        else if (node.children.ContainsKey(word[0]))
        {
            return dfs(word.Substring(1), node.children[word[0]]);
        }
        else
        {
            return false;
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.AddWord(word);
 * bool param_2 = obj.Search(word);
 */
// @lc code=end

