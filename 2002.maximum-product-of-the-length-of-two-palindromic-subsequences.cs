/*
 * @lc app=leetcode id=2002 lang=csharp
 *
 * [2002] Maximum Product of the Length of Two Palindromic Subsequences
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    2 <= s.length <= 12
    so we can use bitmask to represent which bits are used
    First thing to do: for each mask, determine if the mask represents a palindrome O(2 ^ 12)
    Then among the mask, determine if the subMasks of 0 ^ mask are inside the set
    */
    
    /*
    C# program to decide if a string is a palindrome
    */
    private bool IsPalindrome(string s)
    {
        int l = 0, r = s.Length - 1;
        while (l < r)
        {
            if (s[l] != s[r]) return false;
            else
            {
                l++;
                r--;
            }
        }
        return true;
    }

    /*
    Method to return all subsets of set bits of num1 while smaller than num2
    */
    private HashSet<int> SetBits(int num1, int num2)
    {
        HashSet<int> result = new HashSet<int>();
        int temp = num1;
        while (temp > 0)
        {
            if (temp <= num2)
            {
                result.Add(temp);
            }
            temp--;
            temp &= num1;
        }
        return result;
    }

    public int MaxProduct(string s)
    {
        int n = s.Length;
        Dictionary<int, int> palindromes = new Dictionary<int, int>();
        for (int mask = 1; mask < (1 << n); mask++)
        {
            string sMask = "";
            int count = 0;
            for (int i = n - 1; i >= 0; i--)
            {
                if ((mask & (1 << i)) > 0)
                {
                    sMask += s[i];
                    count++;
                }
            }
            if (IsPalindrome(sMask))
            {
                palindromes[mask] = count;
            }
        }

        int result = 0;
        for (int mask = 1; mask < (1 << n); mask++)
        {
            if (palindromes.ContainsKey(mask))
            {
                HashSet<int> antiMaskSet = SetBits(((1 << n) - 1) ^ mask, 1 << n);
                foreach (int aMask in antiMaskSet)
                {
                    if (palindromes.ContainsKey(aMask))
                    {
                        result = Math.Max(result, palindromes[mask] * palindromes[aMask]);
                    }
                }
            }
        }

        return result;
    }
}

// @lc code=end

