/*
 * @lc app=leetcode id=864 lang=csharp
 *
 * [864] Shortest Path to Get All Keys
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int ShortestPathAllKeys(string[] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        string keystring = "";
        int[] start = new int[2];

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (Char.IsLower(grid[i][j]))
                {
                    keystring += grid[i][j];
                }
                else if (grid[i][j] == '@')
                {
                    start[0] = i;
                    start[1] = j;
                }
            }
        }

        char[] keyArray = keystring.ToCharArray();
        keystring = new string(keyArray);
        Dictionary<char, int> keyHash = new Dictionary<char, int>();

        for (int i = 0; i < keystring.Length; i++)
        {
            keyHash[keystring[i]] = i;
        }

        Queue<int[]> dq = new Queue<int[]>();
        HashSet<string> visited = new HashSet<string>();
        int steps = 0;
        int[] state = new int[] { start[0], start[1], 0 };
        dq.Enqueue(state);
        visited.Add($"{state[0]},{state[1]},{state[2]}");
        int[][] neigs = new int[][] { new int[] { 0, 1 }, new int[] { 0, -1 }, new int[] { 1, 0 }, new int[] { -1, 0 } };

        while (dq.Count > 0)
        {
            int size = dq.Count;
            for (int i = 0; i < size; i++)
            {
                int[] node = dq.Dequeue();
                if (node[2] == (1 << keystring.Length) - 1)
                {
                    return steps;
                }
                foreach (int[] neig in neigs)
                {
                    int[] newNode = new int[] { node[0] + neig[0], node[1] + neig[1] };
                    if (newNode[0] >= 0 && newNode[0] < m && newNode[1] >= 0 && newNode[1] < n)
                    {
                        char c = grid[newNode[0]][newNode[1]];
                        if (c == '.' || c == '@' || (Char.IsUpper(c) && (node[2] & (1 << keyHash[Char.ToLower(c)])) != 0))
                        {
                            string newKey = $"{newNode[0]},{newNode[1]},{node[2]}";
                            if (!visited.Contains(newKey))
                            {
                                dq.Enqueue(new int[] { newNode[0], newNode[1], node[2] });
                                visited.Add(newKey);
                            }
                        }
                        else if (Char.IsLower(c))
                        {
                            int newState;
                            if ((node[2] & (1 << keyHash[c])) == 0)
                            {
                                newState = node[2] ^ (1 << keyHash[c]);
                            }
                            else
                            {
                                newState = node[2];
                            }
                            string newKey = $"{newNode[0]},{newNode[1]},{newState}";
                            if (!visited.Contains(newKey))
                            {
                                dq.Enqueue(new int[] { newNode[0], newNode[1], newState });
                                visited.Add(newKey);
                            }
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

