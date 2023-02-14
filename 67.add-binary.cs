/*
 * @lc app=leetcode id=67 lang=csharp
 *
 * [67] Add Binary
 */

// @lc code=start
public class Solution 
{
    public string AddBinary(string a, string b) 
    {
        int na = a.Length;
        int nb = b.Length;
        int carry = 0;
        if (a.Length < b.Length)
        {
            return AddBinary(b, a);
        }
        Stack<string> stack = new Stack<string>();
        for (int i = na - 1; i >= 0; i--)
        {
            int ans;
            if (i >= na - nb)
            {
                carry = Math.DivRem(((int)a[i]) + ((int)b[i - na + nb])- 2*((int)'0') + carry, 2, out ans);
            }
            else
            {
                carry = Math.DivRem(((int)a[i]) - ((int)'0') + carry, 2, out ans);
            }
            stack.Push(ans.ToString());     
        }
        
        if (carry > 0)
        {
            stack.Push("1");
        }
        StringBuilder sb = new StringBuilder();
        while (stack.TryPop(out string s))
        {
            sb.Append(s);
        }
        return sb.ToString();
    }
}
// @lc code=end

