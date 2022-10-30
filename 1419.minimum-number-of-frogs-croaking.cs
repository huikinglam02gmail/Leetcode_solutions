/*
 * @lc app=leetcode id=1419 lang=csharp
 *
 * [1419] Minimum Number of Frogs Croaking
 */

// @lc code=start
public class Solution {
    public int MinNumberOfFrogs(string croakOfFrogs) {
        Dictionary<Char,int> occur = new Dictionary<Char,int>();
        Dictionary<Char,int> frogs = new Dictionary<Char,int>();
        Dictionary<Char,Char> prevChar = new Dictionary<Char,Char>();
        int result = 0;

        occur.Add('c',0);
        occur.Add('r',0);
        occur.Add('o',0);
        occur.Add('a',0);
        occur.Add('k',0);
        frogs.Add('c',0);
        frogs.Add('r',0);
        frogs.Add('o',0);
        frogs.Add('a',0);
        frogs.Add('k',0);
        prevChar.Add('c','k');
        prevChar.Add('r','c');
        prevChar.Add('o','r');
        prevChar.Add('a','o');
        prevChar.Add('k','a');

        foreach (Char c in croakOfFrogs)
        {
            occur[c] += 1;
            if (occur['c'] < occur['r'] || occur['r'] < occur['o'] || occur['o'] < occur['a'] || occur['a'] < occur['k'])
            {
                return -1;
            }
        }
        if (occur['c'] != occur['r'] || occur['c'] != occur['o'] || occur['c'] != occur['a'] || occur['c'] != occur['k'])
            {
                return -1;
            }

        foreach (Char c in croakOfFrogs)
        {
            if (frogs[prevChar[c]] > 0)
            {
                frogs[prevChar[c]] -= 1;
            }
            else
            {
                result += 1;
            }
            frogs[c] += 1;
        }
        return result;
    }
}
// @lc code=end

