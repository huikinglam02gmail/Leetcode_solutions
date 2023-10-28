/*
 * @lc app=leetcode id=1960 lang=csharp
 *
 * [1960] Maximum Product of the Length of Two Palindromic Substrings
 */

// @lc code=start
public class Solution 
{
    public int[] Manacher(string s)
    {
        int n = s.Length;
        int[] LPS = new int[n];
        int C = 0; // center
        int R = 0; // rightmost palindrome
        int j;
        for (int i = 0; i < n; i++)
        {
            if (i < C + R) // if there's an overlap
            {
                j = LPS[C - (i - C)]; // reflect

                if (j < C + R - i) // case A
                {
                    LPS[i] = j;
                    continue;
                }
                else if (j > C + R - i) // case B
                {
                    LPS[i] = C + R - i;
                    continue;
                }
                // case C: do nothing
            }
            else // no overlap
            {
                j = 0;
            }

            while (i - j > 0 && i + j < n - 1 && s[i - j - 1] == s[i + j + 1])
            {
                j++;
            }

            LPS[i] = j;

            if (i + j > C + R)
            {
                C = i;
                R = j;
            }
        }

        return LPS;
    }
    
    public long MaxProduct(string s)
    {
        int n = s.Length;
        int[] LPS = Manacher(s);
        int[] prefix = new int[n];
        int[] suffix = new int[n];

        for (int i = 0; i < n; i++)
        {
            prefix[i + LPS[i]] = Math.Max(prefix[i + LPS[i]], 2 * LPS[i] + 1);
            suffix[i - LPS[i]] = Math.Max(suffix[i - LPS[i]], 2 * LPS[i] + 1);
        }

        for (int i = n - 2; i >= 0; i--)
        {
            prefix[i] = Math.Max(prefix[i], prefix[i + 1] - 2);
        }

        for (int i = 1; i < n; i++)
        {
            suffix[i] = Math.Max(suffix[i], suffix[i - 1] - 2);
        }

        int[] prefixMax = new int[n];
        int[] suffixMax = new int[n];
        int cur = 0;

        for (int i = 0; i < n; i++)
        {
            cur = Math.Max(cur, prefix[i]);
            prefixMax[i] = cur;
        }

        cur = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            cur = Math.Max(cur, suffix[i]);
            suffixMax[i] = cur;
        }

        long result = 0;

        for (int i = 0; i < n - 1; i++)
        {
            result = Math.Max(result, (long)prefixMax[i] * (long)suffixMax[i + 1]);
        }

        return result;
    }
}
// @lc code=end

