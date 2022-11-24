/*
 * @lc app=leetcode id=79 lang=csharp
 *
 * [79] Word Search
 */

// @lc code=start
public class Solution 
{
    char[][] Board;
    int[][] directions;

    public bool dfs(int row, int col, string word)
    {
        if (word.Length == 0)
        {
            return true;
        }
        else if (Board[row][col] == word[0])
        {
            Board[row][col] = '0';
            foreach (int[] dir in directions)
            {
                if (dfs(row + dir[0], col + dir[1], word.Substring(1)))
                {
                    return true;
                }
            }
            Board[row][col] = word[0];
        }
        return false;
    }

    public bool Exist(char[][] board, string word) 
    {
        int m = board.Length;
        int n = board[0].Length;
        directions = new int[4][];
        directions[0] = new int[2] {0, 1};
        directions[1] = new int[2] {0, -1};
        directions[2] = new int[2] {1, 0};
        directions[3] = new int[2] {-1, 0};
        Dictionary<char, int> boardDict = new Dictionary<char, int>();
        Dictionary<char, int> wordDict = new Dictionary<char, int>();
        char[] alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".ToCharArray();
        if (word.Length > m*n)
        {
            return false;
        }

        foreach (char c in alpha)
        {
            boardDict.Add(c, 0);
            wordDict.Add(c, 0);
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                boardDict[board[i][j]]++;
            }
        }

        foreach (char c in word)
        {
            wordDict[c]++;
        }
        
        foreach (char c in alpha)
        {
            if (wordDict[c] > boardDict[c])
            {
                return false;
            }
        }

        if (wordDict[word[0]] > wordDict[word[word.Length-1]])
        {
            char[] charArr = word.ToCharArray();
            Array.Reverse(charArr);
            word = new string(charArr);
        }

        Board = new char[m + 2][];
        Board[0] = new char[n + 2];
        Array.Fill(Board[0], '0');
        Board[m+1] = new char[n + 2];
        Array.Fill(Board[m+1], '0');
        for (int i = 0; i < m; i++)
        {
            Board[i+1] = new char[n+2];
            Board[i+1][0] = '0';
            for (int j = 0; j < n; j++)
            {
                Board[i+1][j+1] = board[i][j];
            }
            Board[i+1][n+1] = '0';
        }

        for (int i = 1; i < m+1; i++)
        {
            for (int j = 1; j < n+1; j++)
            {
                if (dfs(i, j, word))
                {
                    return true;
                }
            }
        }
        return false;
    }
}
// @lc code=end

