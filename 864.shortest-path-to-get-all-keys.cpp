/*
 * @lc app=leetcode id=864 lang=cpp
 *
 * [864] Shortest Path to Get All Keys
 */

// @lc code=start
#include<vector>
#include<string>
#include<iterator>
#include<unordered_map>
#include<unordered_set>
#include<queue>
using std::back_inserter;
using std::copy;
using std::islower;
using std::isupper;
using std::queue;
using std::string;
using std::to_string;
using std::tolower;
using std::unordered_map;
using std::unordered_set;
using std::vector;
class Solution {
public:
    int shortestPathAllKeys(vector<string>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        string keystring = "";
        vector<int> start {-1, -1};

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (islower(grid[i][j]) != 0)
                {
                    keystring += grid[i][j];
                }
                else if (grid[i][j] == '@')
                {
                    start[0] = i;
                    start[1] = j;
                }
            }
        }

        vector<char> keyArray;
        copy(keystring.begin(), keystring.end(), back_inserter(keyArray));
        unordered_map<char, int> keyHash {};

        for (int i = 0; i < keystring.size(); i++)
        {
            keyHash[keystring[i]] = i;
        }

        queue<vector<int>> dq {};
        unordered_set<string> visited {};
        int steps = 0;
        vector<int> state { start[0], start[1], 0 };
        dq.push(state);
        visited.insert(to_string(state[0]) + "," + to_string(state[1]) + "," + to_string(state[2]));
        vector<vector<int>> neigs = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        while (dq.size() > 0)
        {
            int size = dq.size();
            for (int i = 0; i < size; i++)
            {
                vector<int> node = dq.front();
                dq.pop();
                if (node[2] == (1 << keystring.size()) - 1)
                {
                    return steps;
                }
                for (vector<int> neig : neigs)
                {
                    vector<int> newNode  { node[0] + neig[0], node[1] + neig[1] };
                    if (newNode[0] >= 0 && newNode[0] < m && newNode[1] >= 0 && newNode[1] < n)
                    {
                        char c = grid[newNode[0]][newNode[1]];
                        if (c == '.' || c == '@' || (isupper(c) && (node[2] & (1 << keyHash[tolower(c)])) != 0))
                        {
                            string newKey = to_string(newNode[0]) + "," + to_string(newNode[1]) + "," + to_string(node[2]);
                            if (visited.find(newKey) == visited.end())
                            {
                                dq.push(vector<int> { newNode[0], newNode[1], node[2] });
                                visited.insert(newKey);
                            }
                        }
                        else if (islower(c))
                        {
                            int newState;
                            if ((node[2] & (1 << keyHash[c])) == 0)
                            {
                                newState = node[2] ^ (1 << keyHash[c]);
                            }
                            else
                            {
                                newState = node[2];
                            }
                            string newKey = to_string(newNode[0]) + "," + to_string(newNode[1]) + "," + to_string(newState);;
                            if (visited.find(newKey) == visited.end())
                            {
                                dq.push(vector<int> { newNode[0], newNode[1], newState });
                                visited.insert(newKey);
                            }
                        }
                    }
                }
            }
            steps++;
        }

        return -1;
    }
};
// @lc code=end

