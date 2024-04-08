/*
 * @lc app=leetcode id=1700 lang=csharp
 *
 * [1700] Number of Students Unable to Eat Lunch
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountStudents(int[] students, int[] sandwiches) {
        int[] counts = new int[2];
        Queue<int> dq = new Queue<int>();
        foreach (int student in students) {
            counts[student]++;
            dq.Enqueue(student);
        }
        foreach (int sandwich in sandwiches) {
            if (counts[sandwich] == 0) return dq.Count;
            else {
                while (dq.Peek() != sandwich) {
                    dq.Enqueue(dq.Dequeue());
                }
                counts[dq.Dequeue()]--;
            }
        }
        return 0;
    }
}

// @lc code=end

