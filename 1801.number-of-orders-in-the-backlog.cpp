/*
 * @lc app=leetcode id=1801 lang=cpp
 *
 * [1801] Number of Orders in the Backlog
 */

// @lc code=start
#include<vector>
#include<queue>
#include<algorithm>
using std::greater;
using std::min;
using std::priority_queue;
using std::vector;
class Solution {
private:
    long long MOD = 1000000007;

public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        vector<priority_queue<vector<int>, vector<vector<int>>, greater<>>> transactions(2, priority_queue<vector<int>, vector<vector<int>>, greater<>>{});
        for (vector<int> order : orders)
        {
            int a = order[1];
            while (a > 0 && transactions[1 - order[2]].size() > 0 && transactions[1 - order[2]].top()[0] <= (order[2] == 0 ? 1 : -1) * order[0])
            {
                vector<int> dataTop = transactions[1 - order[2]].top();
                transactions[1 - order[2]].pop();
                int deduct = min(dataTop[1], a);
                dataTop[1] -= deduct;
                a -= deduct;
                if (dataTop[1] > 0)
                {
                    transactions[1 - order[2]].push(dataTop);
                }
            }
            if (a > 0)
            {
                transactions[order[2]].push(vector<int>{order[0] * (order[2] == 0 ? -1 : 1), a});
            }
        }

        long long result = 0;
        for (int i = 0; i < 2; i++)
        {
            while (transactions[i].size() > 0)
            {
                result += (long long)(transactions[i].top()[1]);
                result %= MOD;
                transactions[i].pop();
            }
        }
        return (int)result;
    }
};
// @lc code=end

