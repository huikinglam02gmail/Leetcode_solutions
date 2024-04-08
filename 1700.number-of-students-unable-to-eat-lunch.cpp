/*
 * @lc app=leetcode id=1700 lang=cpp
 *
 * [1700] Number of Students Unable to Eat Lunch
 */

// @lc code=start
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        vector<int> counts(2, 0);
        queue<int> dq;
        for (int student : students) {
            counts[student]++;
            dq.push(student);
        }
        for (int sandwich : sandwiches) {
            if (counts[sandwich] == 0) return dq.size();
            else {
                while (dq.front() != sandwich) {
                    dq.push(dq.front());
                    dq.pop();
                }
                counts[dq.front()]--;
                dq.pop();
            }
        }
        return 0;
    }
};

// @lc code=end

