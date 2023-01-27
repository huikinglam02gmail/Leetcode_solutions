/*
 * @lc app=leetcode id=472 lang=csharp
 *
 * [472] Concatenated Words
 */

// @lc code=start
public class TrieNode
{
    public Dictionary<char, TrieNode> children{get; set;}
    public bool isEnd{get; set;}
    public TrieNode()
    {
        children = new Dictionary<char, TrieNode>();
        isEnd = false;
    }
}

public class Trie
{
    public TrieNode root{get; set;}
    public Trie()
    {
        root = new TrieNode();
    }

    public void insert(string word)
    {
        TrieNode node = root;
        foreach (char c in word)
        {
            if (!node.children.ContainsKey(c))
            {
                node.children.Add(c, new TrieNode());
            }
            node = node.children[c];
        }
        node.isEnd = true;
    }
}
public class Solution 
{
    Trie wordSet;
    HashSet<string> failed;
    List<string> result;

    public bool dfs(TrieNode node, string word, int count)
    {
        if (word.Length == 0)
        {
            return count > 1;
        }
        int i = 0;
        while (i < word.Length && node.children.ContainsKey(word[i]))
        {
            node = node.children[word[i]];
            if (node.isEnd && dfs(wordSet.root, word.Substring(i+1), count + 1))
            {
                return true;
            }
            i++;
        }
        return false;
    }

    public IList<string> FindAllConcatenatedWordsInADict(string[] words) 
    {
        wordSet = new Trie();
        result = new List<string>();

        foreach (string word in words)
        {
            wordSet.insert(word);
        }

        foreach (string word in words)
        {
            if (dfs(wordSet.root, word, 0))
            {
                result.Add(word);
            }
        }
        return result;        
    }
}
// @lc code=end

