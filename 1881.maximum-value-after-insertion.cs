/*
 * @lc app=leetcode id=1881 lang=csharp
 *
 * [1881] Maximum Value after Insertion
 */

// @lc code=start
public class Solution
{
    public string MaxValue(string n, int x)
    {
        bool neg = n[0] == '-';
        int i = neg ? 1 : 0;
        bool stop = false;

        while (i < n.Length && !stop)
        {
            if (neg)
                stop = x < int.Parse(n[i].ToString());
            else
                stop = x > int.Parse(n[i].ToString());

            if (!stop)
                i++;
        }

        return n.Substring(0, i) + x.ToString() + n.Substring(i);
    }
}

// @lc code=end

