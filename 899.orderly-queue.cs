/*
 * @lc app=leetcode id=899 lang=csharp
 *
 * [899] Orderly Queue
 */

// @lc code=start
public class Solution {
    public string OrderlyQueue(string s, int k) {
        if (k > 1)
        {
            char[] sArr = s.ToCharArray();
            Array.Sort(sArr);
            return string.Join("", sArr);
        }
        else
        {
            int n = s.Length;
            string[] strArr = new string[n];
            for (int i = 0; i < n; i++)
            {
                strArr[i] = s.Substring(i, n-i) + s.Substring(0, i);
            }
            Array.Sort(strArr);
            return strArr[0];
        }
    }
}
// @lc code=end

