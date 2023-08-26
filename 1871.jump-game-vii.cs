/*
 * @lc app=leetcode id=1871 lang=csharp
 *
 * [1871] Jump Game VII
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public bool CanReach(string s, int minJump, int maxJump) {
        var dq = new Queue<int>();
        dq.Enqueue(0);
        bool result = false;
        
        for (int i = 0; i < s.Length; i++) {
            while (dq.Count > 0 && dq.Peek() < i) {
                dq.Dequeue();
            }
            
            if (s[i] == '0' && dq.Count > 0 && dq.Peek() - maxJump + minJump <= i && i <= dq.Peek()) {
                dq.Enqueue(i + maxJump);
                if (i == s.Length - 1) {
                    result = true;
                }
            }
        }
        
        return result;
    }
}


// @lc code=end

