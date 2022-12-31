/*
 * @lc app=leetcode id=1583 lang=csharp
 *
 * [1583] Count Unhappy Friends
 */

// @lc code=start
public class Solution 
{
    public int UnhappyFriends(int n, int[][] preferences, int[][] pairs) 
    {
        int[][] Preferences = new int[n][];
        int[] partners = new int[n];
        int result = 0;

        for (int i = 0; i < pairs.Length; i++)
        {
            partners[pairs[i][0]] = pairs[i][1];
            partners[pairs[i][1]] = pairs[i][0];
        }


        for (int i = 0; i < preferences.Length; i++)
        {
            Preferences[i] = new int[n];
            Array.Fill(Preferences[i], -1);
            for (int j = 0; j < preferences[i].Length; j++)
            {
                Preferences[i][preferences[i][j]] = j;
            }
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j <n; j++)
            {
                Console.WriteLine($"{i}, {j}, {Preferences[i][j]} ");
            }
        }
        
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (j != partners[i] && i != j && Preferences[i][j] < Preferences[i][partners[i]] && Preferences[j][i] < Preferences[j][partners[j]])
                {
                    result++;
                    break;
                }
            }
            Console.WriteLine($"{i}, {result}");
        }
        return result;
    }
}
// @lc code=end
