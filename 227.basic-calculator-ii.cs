/*
 * @lc app=leetcode id=227 lang=csharp
 *
 * [227] Basic Calculator II
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
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

