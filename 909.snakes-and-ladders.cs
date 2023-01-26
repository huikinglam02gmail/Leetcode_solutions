/*
 * @lc app=leetcode id=909 lang=csharp
 *
 * [909] Snakes and Ladders
 */

// @lc code=start
public class Solution 
{
    public int SnakesAndLadders(int[][] board) 
    {
        List<int> arr = new List<int>();
        Queue<int> queue = new Queue<int>();
        int n = board.Length;
        bool[] visited = new bool[n*n];
        int steps = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            if ((n - 1 - i) % 2 == 0)
            {
                arr = Enumerable.Concat(arr, board[i].ToList()).ToList();
            }
            else
            {
                arr = Enumerable.Concat(arr, board[i].Reverse().ToList()).ToList();
            }
        }    

        queue.Enqueue(0);
        Array.Fill(visited, false);
        visited[0] = true;
        while (queue.Count > 0)
        {
            int queueLength = queue.Count;
            for (int i = 0; i < queueLength; i++)
            {
                int node = queue.Dequeue();
                if (node == n*n - 1)
                {
                    return steps;
                }
                for (int j = 1; j < 7; j++)
                {
                    int nxt = node + j;
                    if (nxt < n*n)
                    {
                        if (arr[nxt] != -1)
                        {
                            nxt = arr[nxt] - 1;
                        }
                        if (!visited[nxt])
                        {
                            queue.Enqueue(nxt);
                            visited[nxt] = true;
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}
// @lc code=end

