/*
 * @lc app=leetcode id=212 lang=csharp
 *
 * [212] Word Search II
 */

// @lc code=start
public class TrieNode
{
    public Dictionary<char, TrieNode> children; 
    public bool isEnd;

    public TrieNode()
    {
        this.children = new Dictionary<char, TrieNode>();
        this.isEnd = false;
    }
}

public class Solution 
{
    HashSet<string> result = new HashSet<string>();
    int[] charWordStart = new int[26];
    char[][] Board;
    TrieNode root = new TrieNode();
    
    public void dfs(int x, int y, TrieNode node, string word)
    {
        if (node.isEnd && !result.Contains(word))
        {
            result.Add(word);
            charWordStart[(int) (word[0] - 'a')] -= 1;
        }

        List<Tuple<int,int>> candidates = new List<Tuple<int,int>>();
        candidates.Add((x-1,y).ToTuple());
        candidates.Add((x+1,y).ToTuple());
        candidates.Add((x,y-1).ToTuple());
        candidates.Add((x,y+1).ToTuple());

        foreach (Tuple<int, int> t in candidates)
        {
            int nx = t.Item1;
            int ny = t.Item2;
            if (nx >= 0 && nx < Board.Length && ny >= 0 && ny < Board[0].Length && node.children.ContainsKey(Board[nx][ny]))
            {
                char c = Board[nx][ny];
                Board[nx][ny] = 'X';
                dfs(nx, ny, node.children[c], word + c);
                Board[nx][ny] = c;
            }
        }
    }
    
    public IList<string> FindWords(char[][] board, string[] words) 
    {
        Board = board;
        int m = board.Length;
        int n = board[0].Length;
        int[] charBoard = new int[26];
        Array.Clear(charBoard, 0, 26);
        foreach (char[] row in board)
        {
            foreach (char c in row)
            {
                charBoard[(int) c - (int) 'a'] += 1;
            }
        }
        foreach (string word in words)
        {
            int[] charWord = new int[26];
            Array.Clear(charWord, 0, 26);
            foreach (char c in word)
            {
                charWord[(int) c - (int) 'a'] += 1;
            }
            
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
            charWordStart[(int) word[0] - (int) 'a'] += 1;
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                char c = Board[i][j];
                if (root.children.ContainsKey(c) && charWordStart[(int) c - (int) 'a'] > 0)
                {
                    Board[i][j] = 'X';
                    dfs(i, j, root.children[c], c.ToString());
                    Board[i][j] = c;
                }
            }
        }
        return result.ToList();
    }
}
// @lc code=end

