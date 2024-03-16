/*
 * @lc app=leetcode id=2069 lang=csharp
 *
 * [2069] Walking Robot Simulation II
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Robot {
    private int w, h, x, y, dir;
    private bool walked;
    private int[][] dirs;
    private string[] dirNames;

    public Robot(int width, int height) {
        w = width;
        h = height;
        x = 0;
        y = 0;
        dir = 0;
        walked = false;
        dirs = new int[][] { new int[] { 1, 0 }, new int[] { 0, 1 }, new int[] { -1, 0 }, new int[] { 0, -1 } };
        dirNames = new string[] { "East", "North", "West", "South" };
    }

    public void Step(int num) {
        num %= 2 * (w + h - 2);
        walked = true;
        for (int i = 0; i < num; i++) {
            if (!(0 <= x + dirs[dir][0] && x + dirs[dir][0] < w && 0 <= y + dirs[dir][1] && y + dirs[dir][1] < h)) {
                dir = (dir + 1) % 4;
            }
            x += dirs[dir][0];
            y += dirs[dir][1];
        }
    }

    public List<int> GetPos() {
        return new List<int> { x, y };
    }

    public string GetDir() {
        if (x == 0 && y == 0) {
            return walked ? "South" : "East";
        } else {
            return dirNames[dir];
        }
    }
}


/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.Step(num);
 * int[] param_2 = obj.GetPos();
 * string param_3 = obj.GetDir();
 */
// @lc code=end

