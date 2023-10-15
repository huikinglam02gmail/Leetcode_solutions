/*
 * @lc app=leetcode id=1947 lang=cpp
 *
 * [1947] Maximum Compatibility Score Sum
 */

// @lc code=start
/**
 * @lc app=leetcode id=1947 lang=cpp
 *
 * [1947] Maximum Compatibility Score Sum
 */

#include <vector>
#include <map>
#include <tuple>
using namespace std;

class Solution {
private:
    vector<vector<int>> students;
    vector<vector<int>> mentors;
    int m;
    int n;
    map<tuple<int, int>, int> memo1;
    map<tuple<int, int>, int> memo;

public:
    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        this->students = students;
        this->mentors = mentors;
        this->m = students.size();
        this->n = students[0].size();
        return Backtracking(0, 0);
    }

private:
    int CompatibilityScore(int i, int j) {
        tuple<int, int> t = make_tuple(i, j);
        if (memo1.find(t) == memo1.end()) {
            int score = 0;
            for (int k = 0; k < n; k++) {
                score += 1 - (students[i][k] ^ mentors[j][k]);
            }
            memo1[t] = score;
        }
        return memo1[t];
    }

    int Backtracking(int studentMask, int mentorMask) {
        tuple<int, int> t = make_tuple(studentMask, mentorMask);
        if (memo.find(t) == memo.end()) {
            int result = 0;

            for (int i = 0; i < m; i++) {
                if ((studentMask & (1 << i)) == 0) {
                    for (int j = 0; j < m; j++) {
                        if ((mentorMask & (1 << j)) == 0) {
                            result = max(result, CompatibilityScore(i, j) + Backtracking(studentMask | (1 << i), mentorMask | (1 << j)));
                        }
                    }
                }
            }

            memo[t] = result;
        }
        return memo[t];
    }
};

// @lc code=end

