/*
 * @lc app=leetcode id=1203 lang=cpp
 *
 * [1203] Sort Items by Groups Respecting Dependencies
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <queue>

class Solution {
public:
    std::vector<int> sortItems(int n, int m, std::vector<int>& group, std::vector<std::vector<int>>& beforeItems) {
        std::vector<std::vector<int>> Groups;
        for (int i = 0; i < m; i++) {
            Groups.push_back({});
        }
        std::vector<int> indexToGroup(n, -1);
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                Groups.push_back({ i });
                indexToGroup[i] = Groups.size() - 1;
            }
            else {
                Groups[group[i]].push_back(i);
                indexToGroup[i] = group[i];
            }
        }

        m = Groups.size();
        std::vector<std::vector<std::vector<int>>> intraGroup(m, std::vector<std::vector<int>>{});
        std::vector<std::vector<int>> interGroup;
        for (int i = 0; i < beforeItems.size(); i++) {
            for (int beforeItem : beforeItems[i]) {
                if (indexToGroup[i] == indexToGroup[beforeItem]) {
                    intraGroup[indexToGroup[i]].push_back(std::vector<int>{beforeItem, i});
                }
                else {
                    interGroup.push_back({ indexToGroup[beforeItem], indexToGroup[i] });
                }
            }
        }

        for (int i = 0; i < m; i++) {
            if (!intraGroup[i].empty()) {
                std::vector<int> bfs = TopoSort(Groups[i], intraGroup[i]);
                if (bfs.size() == Groups[i].size()) {
                    Groups[i] = bfs;
                }
                else {
                    return {};
                }
            }
        }

        std::vector<int> groupId(m);
        for (int i = 0; i < m; i++) {
            groupId[i] = i;
        }

        std::vector<int> bfs = TopoSort(groupId, interGroup);
        std::vector<int> result;
        if (bfs.size() == m) {
            for (int i : bfs) {
                for (int j : Groups[i]) {
                    result.push_back(j);
                }
            }
        }
        return result;
    }
    
    std::vector<int> TopoSort(std::vector<int>& allElements, std::vector<std::vector<int>>& order) {
        std::unordered_map<int, std::vector<int>> G;
        std::unordered_map<int, int> degree;
        
        for (std::vector<int>& kvp : order) {
            int j = kvp[0], k = kvp[1];
            if (G.find(j) == G.end()) {
                G[j] = {};
            }
            if (degree.find(k) == degree.end()) {
                degree[k] = 0;
            }
            G[j].push_back(k);
            degree[k]++;
        }
        
        std::queue<int> queue;
        std::vector<int> bfs;
        for (int j : allElements) {
            if (degree.find(j) == degree.end()) {
                queue.push(j);
                bfs.push_back(j);
            }
        }

        while (!queue.empty()) {
            int node = queue.front();
            queue.pop();
            if (G.find(node) != G.end()) {
                for (int k : G[node]) {
                    degree[k]--;
                    if (degree[k] == 0) {
                        queue.push(k);
                        bfs.push_back(k);
                    }
                }
            }
        } 
        return bfs;
    }
};

// @lc code=end

