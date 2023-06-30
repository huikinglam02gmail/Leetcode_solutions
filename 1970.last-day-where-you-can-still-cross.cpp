#include<vector>
#include<algorithm>
#include<queue>
using std::fill;
using std::pair;
using std::queue;
using std::vector;
class Solution {
private:
    bool CanPass(const vector<bool>& sea, int Row, int Col)
    {
        vector<bool> visited(Row * Col, false);
        queue<int> dq {};
        for (int j = 0; j < Col; j++)
        {
            if (!sea[j])
            {       
                dq.push(j);
                visited[j] = true;
            }
        }
        while (dq.size() > 0)
        {
            int node = dq.front();
            dq.pop();
            vector<pair<int, int>> neigs = {{ (node / Col) - 1, node % Col }, { (node / Col) + 1, node % Col }, { node / Col, node % Col - 1 }, { node / Col, node % Col + 1 }};
            for (pair<int, int> neig : neigs)
            {
                if (neig.first >= 0 && neig.first < Row && neig.second >= 0 && neig.second < Col && !visited[neig.first * Col + neig.second] && !sea[neig.first * Col + neig.second])
                {
                    if (neig.first == Row - 1)
                    {
                        return true;
                    }
                    else
                    {
                        visited[neig.first * Col + neig.second] = true;
                        dq.push(neig.first * Col + neig.second);                        
                    }
                }
            }
        }
        return false;
    }

public:
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        vector<bool> sea(row * col, false);
        int l = 0;
        int r = row * col;
        while (l < r)
        {
            int mid = l + (r - l) / 2;
            fill(sea.begin(), sea.end(), false);
            for (int i = 0; i < mid; i++)
            {
                sea[(cells[i][0] - 1) * col + cells[i][1] - 1] = true;
            }
            if (CanPass(sea, row, col))
            {
                l = mid + 1;
            }
            else
            {
                r = mid;
            }
        }
        return l - 1;
    }
};