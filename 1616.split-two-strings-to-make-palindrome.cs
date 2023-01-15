/*
 * @lc app=leetcode id=1616 lang=csharp
 *
 * [1616] Split Two Strings to Make Palindrome
 */

// @lc code=start
public class Solution 
{
    bool IsPalindrome(string s) 
    {
        int i = 0, j = s.Length - 1;
        while (i < j) 
        {
            if (s[i] != s[j]) 
            {
                return false;
            }
            else 
            {
                i++;
                j--;
            }
        }
        return true;
    }
    
    public bool canFormPalindrome(string s1, string s2)
    {
        int n = s1.Length;
        int l = 0;
        int r = n - 1;
        bool canForm = true;
        while (l < n / 2 && s1[l] == s2[r])
        {
            l++;
            r--;
        }            
        if (l < (n / 2))
        {
            canForm = IsPalindrome(s1.Substring(l,n - 2*l)) || IsPalindrome(s2.Substring(l,n - 2*l));
        }
        return canForm;
    }
         

    public bool CheckPalindromeFormation(string a, string b) 
    {
        return canFormPalindrome(a, b) || canFormPalindrome(b, a);
    }
}
// @lc code=end

