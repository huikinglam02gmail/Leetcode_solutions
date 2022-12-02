/*
 * @lc app=leetcode id=1505 lang=csharp
 *
 * [1505] Minimum Possible Integer After at Most K Adjacent Swaps On Digits
 */

// @lc code=start
public class Solution 
{
    public string MinInteger(string num, int k) 
    {
        int n = num.Length;
        if (k <= 0)
        {
            return num;
        }
        else if (k > n*(n-1)/2)
        {
            char[] numArray = num.Select(s => s).ToArray();
            Array.Sort(numArray);
            return String.Join("", numArray);
        }
        else
        {
            int i = 0;
            while (i < 10)
            {
                int index = num.IndexOf(i.ToString());
                if (index >= 0 && index <= k)
                {
                    return num[index] + MinInteger(num.Substring(0, index) + num.Substring(index + 1), k - index);
                }
                else
                {
                    i++;
                }
            }
        }
        return "";
    }
}
// @lc code=end

