/*
 * @lc app=leetcode id=1433 lang=csharp
 *
 * [1433] Check If a String Can Break Another String
 */

// @lc code=start
public class Solution {
    public bool CheckIfCanBreak(string s1, string s2) {
        int n = s1.Length;
        char[] s1Arr = s1.ToCharArray();
        char[] s2Arr = s2.ToCharArray();

        Array.Sort(s1Arr);
        Array.Sort(s2Arr);
        int count1 = 0;
        int count2 = 0;
        for (int i = 0; i < n; i++)
        {
            if (s1Arr[i] > s2Arr[i])
            {
                count1 += 1;
            }
            else if (s1Arr[i] < s2Arr[i])
            {
                count2 += 1;
            }
        }
        return (count1 == 0 || count2 == 0);
    }
}
// @lc code=end

