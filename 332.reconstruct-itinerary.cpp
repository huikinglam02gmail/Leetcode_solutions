/*
 * @lc app=leetcode id=332 lang=cpp
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>

using std::all_of;
using std::pair;
using std::sort;
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
private:
    unordered_map<string, vector<pair<int, string>>> graph;
    bool found;
    string result;
    vector<bool> used;

public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        graph.clear();
        found = false;
        result = "";
        used.assign(tickets.size(), false);

        std::sort(tickets.begin(), tickets.end());

        for (int i = 0; i < tickets.size(); i++) {
            string from = tickets[i][0];
            string to = tickets[i][1];
            graph[from].push_back(std::make_pair(i, to));
        }

        DFS("JFK", "");

        vector<string> stringList;
        int i = 0;
        while (i < result.length()) {
            stringList.push_back(result.substr(i, 3));
            i += 3;
        }

        return stringList;
    }

private:
    void DFS(const string& current, const string& itinerary) {
        if (all_of(used.begin(), used.end(), [](bool val) { return val == true; })) {
            result = itinerary + current;
            found = true;
        }
        else if (graph.find(current) != graph.end() && !found) {
            for (const auto& edge : graph[current]) {
                int id = edge.first;
                string nxt = edge.second;
                if (!used[id] && !found) {
                    used[id] = true;
                    DFS(nxt, itinerary + current);
                    used[id] = false;
                }
            }
        }
    }
};
// @lc code=end

