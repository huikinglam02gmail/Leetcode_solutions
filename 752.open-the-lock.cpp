/*
 * @lc app=leetcode id=752 lang=cpp
 *
 * [752] Open the Lock
 */

// @lc code=start
#include <vector>
#include <queue>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    /*
    As hinted, this is an undirected graph BFS problem
    Treat each status as a node
    Graph connection: at each index, it can be arrive at the adjacent integer at each digit
    "0000" to "0001", "0009", "0010","0090",.. etc
    Therefore the problem is just asking for reachability
    */
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> deadendsSet(deadends.begin(), deadends.end());
        // BFS from "0000"
        queue<string> dq;
        unordered_set<string> visited;
        int steps = 0;
        dq.push("0000");
        visited.insert("0000");
        while (!dq.empty()) {
            int count = dq.size();
            for (int i = 0; i < count; i++) {
                string node = dq.front();
                dq.pop();
                if (node == target) return steps;
                if (deadendsSet.find(node) != deadendsSet.end()) continue;
                for (int j = 0; j < 4; j++) {
                    string nodeUp = node;
                    string nodeDown = node;
                    if (node[j] == '9') {
                        nodeUp[j] = '0';
                    } else {
                        nodeUp[j]++;
                    }
                    if (node[j] == '0') {
                        nodeDown[j] = '9';
                    } else {
                        nodeDown[j]--;
                    }
                    if (visited.find(nodeUp) == visited.end()) {
                        dq.push(nodeUp);
                        visited.insert(nodeUp);
                    }
                    if (visited.find(nodeDown) == visited.end()) {
                        dq.push(nodeDown);
                        visited.insert(nodeDown);
                    }
                }
            }
            steps++;
        }
        return -1;
    }
};

// @lc code=end

