/*
 * @lc app=leetcode id=5 lang=csharp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
public class Solution
{
    public string LongestPalindrome(string s)
    {
        // Modify the string so that it's always odd
        string newString = "|";
        foreach (char c in s)
        {
            newString += c + "|";
        }

        int n = newString.Length;
        int[] lps = new int[n];
        int center = 0, right = 0; // Center and right boundary of the rightmost palindrome

        for (int i = 0; i < n; i++)
        {
            if (i < center + right) // If there's an overlap
            {
                int j = lps[center - (i - center)]; // Reflect

                if (j < center + right - i) // Case A
                {
                    lps[i] = j;
                    continue;
                }
                else if (j > center + right - i) // Case B
                {
                    lps[i] = center + right - i;
                    continue;
                }
                else // Case C
                {
                }
            }
            else // No overlap
            {
                int j = 0;
            }

            while (i - lps[i] > 0 && i + lps[i] < n - 1 && newString[i - lps[i] - 1] == newString[i + lps[i] + 1])
            {
                lps[i]++;
            }

            if (i + lps[i] > center + right)
            {
                center = i;
                right = lps[i];
            }
        }

        int maxLength = 0;
        int maxIndex = 0;

        for (int i = 0; i < n; i++)
        {
            if (lps[i] > maxLength)
            {
                maxLength = lps[i];
                maxIndex = i;
            }
        }

        return newString.Substring(maxIndex - maxLength, 2 * maxLength + 1).Replace("|", string.Empty);
    }
}

// @lc code=end

