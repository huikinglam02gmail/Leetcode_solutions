/*
 * @lc app=leetcode id=1728 lang=csharp
 *
 * [1728] Cat and Mouse II
 */

// @lc code=start

using System;
using System.Collections.Generic;

public class Solution
{
    

    public bool CanMouseWin(string[] grid, int catJump, int mouseJump)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] mouse = new int[2];
        int[] cat = new int[2];
        int[] food = new int[2];

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 'M')
                    mouse = new int[] { i, j };
                else if (grid[i][j] == 'F')
                    food = new int[] { i, j };
                else if (grid[i][j] == 'C')
                    cat = new int[] { i, j };
            }
        }

        HashSet<Tuple<int, int>> PrevPositions(int x, int y, int jump)
        {
            HashSet<Tuple<int, int>> result = new HashSet<Tuple<int, int>>();
            int[][] directions = new int[][] { new int[] { 0, 1 }, new int[] { 0, -1 }, new int[] { 1, 0 }, new int[] { -1, 0 } };

            foreach (int[] direction in directions)
            {
                for (int i = 0; i <= jump; i++)
                {
                    int newX = x + direction[0] * i;
                    int newY = y + direction[1] * i;
                    if (!(newX >= 0 && newX < m && newY >= 0 && newY < n) || grid[newX][newY] == '#')
                        break;
                    result.Add(new Tuple<int, int> ( newX, newY ));
                }
            }

            return result;
        }

        Dictionary<Tuple<int, int, int, int, int>, int> cache = new Dictionary<Tuple<int, int, int, int, int>, int>();
        Dictionary<Tuple<int, int>, HashSet<Tuple<int, int>>> GraphMouse = new Dictionary<Tuple<int, int>, HashSet<Tuple<int, int>>>();
        Dictionary<Tuple<int, int>, HashSet<Tuple<int, int>>> GraphCat = new Dictionary<Tuple<int, int>, HashSet<Tuple<int, int>>>();
        Queue<Tuple<int, int, int, int, int>> dq = new Queue<Tuple<int, int, int, int, int>>();

        for (int r = 0; r < m; r++)
        {
            for (int c = 0; c < n; c++)
            {
                if (grid[r][c] == '#')
                {
                    continue;
                }                    
                GraphMouse[ new Tuple<int, int>(r, c)] = PrevPositions(r, c, mouseJump);
                GraphCat[new Tuple<int, int>(r, c)] = PrevPositions(r, c, catJump);
                for (int turn = 0; turn < 2; turn++)
                {
                    if (!cache.ContainsKey(new Tuple<int, int, int, int, int>(r, c, r, c, turn)))
                    {
                        cache.Add(new Tuple<int, int, int, int, int>(r, c, r, c, turn), 0);
                    }
                    if (!cache.ContainsKey(new Tuple<int, int, int, int, int>(r, c, food[0], food[1], turn)))
                    {
                        cache.Add(new Tuple<int, int, int, int, int>(r, c, food[0], food[1], turn), 0);
                    }
                    if (!cache.ContainsKey(new Tuple<int, int, int, int, int>(food[0], food[1], r, c, turn)))
                    {
                        cache.Add(new Tuple<int, int, int, int, int>(food[0], food[1], r, c, turn), 0);
                    }       
                    cache[new Tuple<int, int, int, int, int>(r, c, r, c, turn)] = 2;             
                    cache[new Tuple<int, int, int, int, int>(r, c, food[0], food[1], turn)] = 2;
                    cache[new Tuple<int, int, int, int, int>(food[0], food[1], r, c, turn)] = 1;
                    dq.Enqueue(new Tuple<int, int, int, int, int>(food[0], food[1], r, c, turn));
                }
            }
        }

        while (dq.Count > 0)
        {
            Tuple<int, int, int, int, int> t = dq.Dequeue();
            if (t.Item5 == 0)
            {
                foreach (Tuple<int, int> prevMouse in GraphMouse[new Tuple<int, int>(t.Item1, t.Item2)])
                {
                    Tuple<int, int, int, int, int> lastState = new Tuple<int, int, int, int, int>(prevMouse.Item1, prevMouse.Item2, t.Item3, t.Item4, 1);
                    if (!cache.ContainsKey(lastState))
                    {
                        cache.Add(lastState, 0);
                    }
                    if (cache[lastState] > 0)
                        continue;
                    else
                    {
                        cache[lastState] = 1;
                        dq.Enqueue(lastState);
                    }
                }
            }
            else
            {
                foreach (Tuple<int, int> prevCat in GraphCat[new Tuple<int, int>(t.Item3, t.Item4)])
                {
                    Tuple<int, int, int, int, int> lastState = new Tuple<int, int, int, int, int>(t.Item1, t.Item2, prevCat.Item1, prevCat.Item2, 0);
                    if (!cache.ContainsKey(lastState))
                    {
                        cache.Add(lastState, 0);
                    }
                    if (cache[lastState] > 0)
                    {
                        continue;                        
                    }
                    else
                    {
                        cache[lastState] -= 1;
                        if (cache[lastState] == -GraphCat[new Tuple<int, int>(prevCat.Item1, prevCat.Item2)].Count)
                        {
                            cache[lastState] = 1;
                            dq.Enqueue(lastState);
                        }
                    }
                }
            }
        }

        return cache.TryGetValue(new Tuple<int, int, int, int, int>(mouse[0], mouse[1], cat[0], cat[1], 1), out int result) && result == 1;
    }
}

// @lc code=end

