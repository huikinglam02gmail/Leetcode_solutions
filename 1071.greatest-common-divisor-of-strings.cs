/*
 * @lc app=leetcode id=1071 lang=csharp
 *
 * [1071] Greatest Common Divisor of Strings
 */

// @lc code=start
public class Solution 
{    
    public string GcdOfStrings(string str1, string str2) 
    {
        int l1 = str1.Length;
        int l2 = str2.Length;
        int start = Math.Min(l1, l2);

        for (int i = start; i > 0; i--)
        {
            if (l1  % i == 0 && l2 % i == 0)
            {
                int j1 = 0;
                int j2 = 0;
                string ss = str1.Substring(j1, j1 + i);
                while (j1 <= l1 - i && str1.Substring(j1, i).Equals(ss))
                {
                    j1 += i;
                }
                while (j2 <= l2 - i && str2.Substring(j2, i).Equals(ss))
                {
                    j2 += i;
                }
                if (j1 == l1 && j2 == l2)
                {
                    return ss;
                }
            }
        }  
        return string.Empty; 
    }
}
// @lc code=end

