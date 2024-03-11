/*
 * @lc app=leetcode id=2059 lang=cpp
 *
 * [2059] Minimum Operations to Convert Number
 */

// @lc code=start
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minimumOperations(vector<int>& nums, int start, int goal) {
        vector<bool> visited(1001,false);
        int ans = 0;
        queue<int> q;
        q.push(start);
        while(!q.empty()){
            int size = q.size();
            while(size--){
                int node = q.front(); 
                q.pop();
                if(node==goal) return ans;
                if(node>1000 || node<0 || visited[node])
                    continue;
                visited[node]=true;
                for(int i = 0;i < nums.size(); ++i){
                    int a = node + nums[i];
                    int b = node - nums[i];
                    int c = node ^ nums[i];
                    for(auto j : {a,b,c})
                            q.push(j);
                }
            }
            ans++;
        }
        return -1;
    }
};

// @lc code=end

