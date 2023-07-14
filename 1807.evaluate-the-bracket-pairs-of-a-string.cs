/*
 * @lc app=leetcode id=1807 lang=csharp
 *
 * [1807] Evaluate the Bracket Pairs of a String
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    use stack to hold previous string, when seeing "(". pop when seeing ")"
    */
    public string Evaluate(string s, IList<IList<string>> knowledge) {
        Dictionary<string, string> hashTable = new Dictionary<string, string>();
        
        foreach (var pair in knowledge) {
            string key = pair[0];
            string value = pair[1];
            hashTable[key] = value;
        }
        
        Stack<string> stack = new Stack<string>();
        string current = "";
        
        foreach (char c in s) {
            if (c == '(') {
                stack.Push(current);
                current = "";
            }
            else if (c == ')') {
                current = stack.Pop() + hashTable.GetValueOrDefault(current, "?");
            }
            else {
                current += c;
            }
        }
        
        return current;
    }
}

// @lc code=end

