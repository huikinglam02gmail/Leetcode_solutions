/*
 * @lc app=leetcode id=345 lang=csharp
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start
public class Solution {
    public string ReverseVowels(string s) {
        HashSet<char> vowels = new HashSet<char>();
        string Vowels = "aeiouAEIOU";
        foreach (char c in Vowels)
        {
            vowels.Add(c);
        }
        int left = 0;
        int right = s.Length - 1;
        char[] arr = s.ToCharArray();
        while (left < right)
        {
            if (!vowels.Contains(arr[left]))
            {
                left += 1;
            }
            else if (!vowels.Contains(arr[right]))
            {
                right -= 1;
            }
            else
            {
                char temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        return new string(arr);
    }
}
// @lc code=end

