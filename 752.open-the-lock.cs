/*
 * @lc app=leetcode id=752 lang=csharp
 *
 * [752] Open the Lock
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    As hinted, this is an undirected graph BFS problem
    Treat each status as a node
    Graph connection: at each index, it can be arrive at the adjacent integer at each digit
    "0000" to "0001", "0009", "0010","0090",.. etc
    Therefore the problem is just asking for reachability
    */
    public int OpenLock(string[] deadends, string target) {
        HashSet<string> deadendsSet = new HashSet<string>(deadends);
        // BFS from "0000"
        Queue<string> dq = new Queue<string>();
        HashSet<string> visited = new HashSet<string>();
        int steps = 0;
        dq.Enqueue("0000");
        visited.Add("0000");
        while (dq.Count > 0) {
            int count = dq.Count;
            for (int i = 0; i < count; i++) {
                string node = dq.Dequeue();
                if (node == target) return steps;
                if (deadendsSet.Contains(node)) continue;
                for (int j = 0; j < 4; j++) {
                    string nodeUp = node.Substring(0, j) + (node[j] == '9' ? '0' : (char)(node[j] + 1)) + node.Substring(j + 1);
                    string nodeDown = node.Substring(0, j) + (node[j] == '0' ? '9' : (char)(node[j] - 1)) + node.Substring(j + 1);
                    if (!visited.Contains(nodeUp)) {
                        dq.Enqueue(nodeUp);
                        visited.Add(nodeUp);
                    }
                    if (!visited.Contains(nodeDown)) {
                        dq.Enqueue(nodeDown);
                        visited.Add(nodeDown);
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}

// @lc code=end

