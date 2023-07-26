/*
 * @lc app=leetcode id=1825 lang=cpp
 *
 * [1825] Finding MK Average
 */

// @lc code=start
#include <queue>
#include <set>
using namespace std;

class MKAverage {
/*
    We use two sets of size k and one set of size m to store the nodes. When we delete a previous node, we first check if it is in the left and right trees. If so, update the trees.
*/
private:
    set<pair<int, int>> tree;
    set<pair<int, int>> left;
    set<pair<int, int>> right;
    long long Total;
    long long leftSum;
    long long rightSum;
    int index;
    int m;
    int k;
    queue<pair<int, int>> q;

    void deleteNode(int num, int index)
    {
        pair<int, int> nodeToRemove = make_pair(num, index);
        if (left.find(nodeToRemove) != left.end())
        {
            pair<int, int> nodeToInsert = *next(tree.find(*left.rbegin()), 1);
            left.insert(nodeToInsert);
            leftSum -= (long long)num;
            leftSum += (long long)nodeToInsert.first;
            left.erase(nodeToRemove);
        }
        if (right.find(nodeToRemove) != right.end())
        {
            pair<int, int> nodeToInsert = *prev(tree.find(*right.begin()), 1);
            right.insert(nodeToInsert);
            rightSum -= (long long)num;
            rightSum += (long long)nodeToInsert.first;
            right.erase(nodeToRemove);
        }

        tree.erase(nodeToRemove);
        Total -= (long long)num;
    }

    void insertNode(int num, int index)
    {
        pair<int, int> nodeToInsert = make_pair(num, index);
        if (left.size() < k || left.lower_bound(nodeToInsert) != left.end())
        {
            if (left.size() == k)
            {
                pair<int, int> nodeToRemove = *left.rbegin();
                left.erase(nodeToRemove);
                leftSum -= (long long)nodeToRemove.first;                                
            }
            left.insert(nodeToInsert);
            leftSum += (long long)num;
         
        }
        if (right.size() < k || right.upper_bound(nodeToInsert) != right.begin())
        {
            if (right.size() == k)
            {
                pair<int, int> nodeToRemove = *right.begin();
                right.erase(nodeToRemove);
                rightSum -= (long long)nodeToRemove.first;                             
            }
            right.insert(nodeToInsert);
            rightSum += (long long)num;            
        }

        tree.insert(nodeToInsert);
        Total += (long long)num;
    }

public:
    MKAverage(int m, int k) {
        tree = set<pair<int, int>>{};
        left = set<pair<int, int>>{};
        right = set<pair<int, int>>{};
        q = queue<pair<int, int>>{};
        Total = (long long)0;
        leftSum = (long long)0;
        rightSum = (long long)0;
        index = -1;
        this->m = m;
        this->k = k;
    }

    void addElement(int num) {
        index++;
        if (q.size() == m)
        {
            pair<int, int> element = q.front();
            q.pop();
            deleteNode(element.first, element.second);
        }
        q.push(make_pair(num, index));
        insertNode(num, index);
    }

    int calculateMKAverage() {
        return tree.size() < m ? -1 : (Total - leftSum - rightSum) / (long long)(m - 2 * k);
    }
};


/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */
// @lc code=end