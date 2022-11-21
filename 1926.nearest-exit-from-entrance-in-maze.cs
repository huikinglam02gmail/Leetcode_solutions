/*
 * @lc app=leetcode id=1926 lang=csharp
 *
 * [1926] Nearest Exit from Entrance in Maze
 */

// @lc code=start
public class Solution 
{
    public int NearestExit(char[][] maze, int[] entrance) 
    {
        Queue<int[]> queue = new Queue<int[]>();
        int steps = 0;
        int m = maze.Length;
        int n = maze[0].Length; 
        queue.Enqueue(entrance);
        maze[entrance[0]][entrance[1]] = '+';

        while (queue.Count() > 0)
        {
            int l = queue.Count();
            for (int i = 0; i < l; i++)
            {
                int[] node = queue.Dequeue();
                int[][] neigs = new int[4][];
                for (int j = 0; j < 4; j++)
                {
                    neigs[j] = new int[2];
                    if (j == 0)
                    {
                        neigs[j][0] = node[0] + 1;
                        neigs[j][1] = node[1];
                    }
                    else if (j == 1)
                    {
                        neigs[j][0] = node[0] - 1;
                        neigs[j][1] = node[1];                        
                    }
                    else if (j == 2)
                    {
                        neigs[j][0] = node[0];
                        neigs[j][1] = node[1] + 1;
                    }
                    else
                    {
                        neigs[j][0] = node[0];
                        neigs[j][1] = node[1] - 1;                        
                    }
                }
                foreach (int[] neig in neigs)
                {
                    int xn = neig[0];
                    int yn = neig[1];
                    if (xn >= 0 && yn >= 0 && xn < m && yn < n && maze[xn][yn] == '.')
                    {
                        if (xn == 0 || yn == 0 || xn == m-1 || yn == n-1)
                        {
                            return steps + 1;
                        }
                        else
                        {
                            queue.Enqueue(neig);
                            maze[xn][yn] = '+';
                        }
                    }
                }
            }
            steps += 1;
        }
        return -1; 
    }
}
// @lc code=end

