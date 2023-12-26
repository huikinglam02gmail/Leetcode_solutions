/*
 * @lc app=leetcode id=2030 lang=csharp
 *
 * [2030] Smallest K-Length Subsequence With Occurrences of a Letter
 */

// @lc code=start
public class Solution {
    public string SmallestSubsequence(string s, int k, char letter, int repetition) {
        Stack<char> stack = new Stack<char>();
        int n = s.Length;
        int usableLetterBehind = s.Count(c => c == letter);

        for (int i = 0; i < n; i++) {
            char c = s[i];
            while (stack.Count > 0 && c < stack.Peek() && n - i + stack.Count > k && (stack.Peek() != letter || usableLetterBehind > repetition)) {
                if (stack.Peek() == letter) repetition += 1;
                stack.Pop();
            }

            if (c == letter) usableLetterBehind -= 1;

            if (stack.Count < k) {
                if (c == letter) {
                    stack.Push(c);
                    repetition -= 1;
                } else if (k - stack.Count > repetition) {
                    stack.Push(c);
                }
            }
        }

        return new string(stack.Reverse().ToArray());
    }
}
// @lc code=end

