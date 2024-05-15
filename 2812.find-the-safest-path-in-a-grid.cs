/*
 * @lc app=leetcode id=2812 lang=csharp
 *
 * [2812] Find the Safest Path in a Grid
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private int[][] minD;
    private int n;

    public bool CanReach(int thres) {
        var dq = new Queue<(int, int)>();
        var visited = new bool[this.n, this.n];

        if (this.minD[0][0] >= thres) {
            dq.Enqueue((0, 0));
            visited[0, 0] = true;
        }

        while (dq.Count > 0) {
            var (x, y) = dq.Dequeue();

            if (x == this.n - 1 && y == this.n - 1) return true;

            var neigs = new List<(int, int)> {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)};

            foreach (var (nx, ny) in neigs) {
                if (nx >= 0 && nx < this.n && ny >= 0 && ny < this.n && !visited[nx, ny] && this.minD[nx][ny] >= thres) {
                    visited[nx, ny] = true;
                    dq.Enqueue((nx, ny));
                }
            }
        }

        return false;
    }

    public int MaximumSafenessFactor(IList<IList<int>> grid) {
        this.n = grid.Count;
        this.minD = new int[this.n][];

        for (int i = 0; i < this.n; i++) {
            this.minD[i] = new int[this.n];
            for (int j = 0; j < this.n; j++) {
                this.minD[i][j] = int.MaxValue;
            }
        }

        var dq = new Queue<(int, int)>();

        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.n; j++) {
                if (grid[i][j] == 1) {
                    dq.Enqueue((i, j));
                    this.minD[i][j] = 0;
                }
            }
        }

        int steps = 1;
        while (dq.Count > 0) {
            int count = dq.Count;
            for (int k = 0; k < count; k++) {
                var (x, y) = dq.Dequeue();
                var neigs = new List<(int, int)> {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)};

                foreach (var (nx, ny) in neigs) {
                    if (nx >= 0 && nx < this.n && ny >= 0 && ny < this.n && this.minD[nx][ny] == int.MaxValue) {
                        this.minD[nx][ny] = steps;
                        dq.Enqueue((nx, ny));
                    }
                }
            }
            steps++;
        }

        int l = 0, r = 2 * this.n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            bool canReach = CanReach(mid);
            if (canReach) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l - 1;
    }
}

// @lc code=end

