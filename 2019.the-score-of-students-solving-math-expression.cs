/*
 * @lc app=leetcode id=2019 lang=csharp
 *
 * [2019] The Score of Students Solving Math Expression
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<string, HashSet<int>> memo = new Dictionary<string, HashSet<int>>();

    public int ScoreOfStudents(string s, int[] answers) {
        Dictionary<int, int> possibleAnswers = new Dictionary<int, int>();
        possibleAnswers.Add(Calculate(s), 5);
        HashSet<int> wrongAnswers = DP(s);

        foreach (var ans in wrongAnswers) {
            if (!possibleAnswers.ContainsKey(ans)) {
                possibleAnswers[ans] = 2;
            }
        }

        int result = 0;
        foreach (var ans in answers) {
            result += possibleAnswers.TryGetValue(ans, out int value) ? value : 0;
        }

        return result;
    }

    private HashSet<int> DP(string s) {
        if (!s.Contains('+') && !s.Contains('*')) {
            return new HashSet<int> { Int32.Parse(s) };
        } else {
            if (memo.ContainsKey(s)) {
                return memo[s];
            }

            List<int> opIndices = new List<int>();
            for (int i = 0; i < s.Length; i++) {
                if (s[i] == '+' || s[i] == '*') {
                    opIndices.Add(i);
                }
            }

            HashSet<int> result = new HashSet<int>();
            foreach (int i in opIndices) {
                HashSet<int> lSet = DP(s.Substring(0, i));
                HashSet<int> rSet = DP(s.Substring(i + 1));
                foreach (int l in lSet) {
                    foreach (int r in rSet) {
                        if (s[i] == '+' && l + r <= 1000) {
                            result.Add(l + r);
                        }
                        if (s[i] == '*' && l * r <= 1000) {
                            result.Add(l * r);
                        }
                    }
                }
            }

            memo[s] = result;
            return result;
        }
    }

    private Stack<int> numStack = new Stack<int>();
    private Stack<char> opStack = new Stack<char>();

    private int Calculation(int current) {
        char oldOp = opStack.Pop();
        int oldCurrent = numStack.Pop();
        if (oldOp == '+') {
            current += oldCurrent;
        } else if (oldOp == '-') {
            current = -current + oldCurrent;
        } else if (oldOp == '*') {
            current *= oldCurrent;
        } else {
            current = oldCurrent / current;
        }
        return current;
    }

    public int Calculate(string s) {
        int current = 0;
        Dictionary<char, int> priority = new Dictionary<char, int>() {
            {'+', 0},
            {'-', 0},
            {'*', 1},
            {'/', 1}
        };

        foreach (char c in s) {
            if (char.IsDigit(c)) {
                current *= 10;
                current += c - '0';
            } else if (c == '+' || c == '-' || c == '*' || c == '/') {
                while (opStack.Count > 0 && priority[opStack.Peek()] >= priority[c]) {
                    current = Calculation(current);
                }
                numStack.Push(current);
                opStack.Push(c);
                current = 0;
            }
        }

        while (opStack.Count > 0) {
            current = Calculation(current);
        }

        return current;
    }
}

// @lc code=end

