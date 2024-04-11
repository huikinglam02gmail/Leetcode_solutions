/*
 * @lc app=leetcode id=402 lang=csharp
 *
 * [402] Remove K Digits
 */

// @lc code=start
public class Solution {
    public string RemoveKdigits(string num, int k) {
        var stack = new List<char>();

        foreach (char c in num) {
            while (stack.Count > 0 && stack.Last() > c && k > 0) {
                stack.RemoveAt(stack.Count - 1);
                k--;
            }
            stack.Add(c);
        }

        while (k > 0) {
            stack.RemoveAt(stack.Count - 1);
            k--;
        }

        if (stack.Count == 0) {
            return "0";
        } else {
            StringBuilder sb = new StringBuilder();
            foreach (char c in stack) {
                sb.Append(c);
            }
            int i = 0;
            while (i < sb.Length && sb[i] == '0') {
                i++;
            }
            if (i == sb.Length) {
                return "0";
            } else {
                return sb.ToString().Substring(i);
            }
        }
    }
}

// @lc code=end

