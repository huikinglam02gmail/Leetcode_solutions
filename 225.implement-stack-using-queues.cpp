/*
 * @lc app=leetcode id=225 lang=cpp
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start
#include <queue>

class MyStack {
private:
    std::queue<int> queue1;
    std::queue<int> queue2;

public:
    MyStack() {
        queue1 = std::queue<int>();
        queue2 = std::queue<int>();
    }

    void push(int x) {
        queue2.push(x);
        while (!queue1.empty()) {
            int y = queue1.front();
            queue1.pop();
            queue2.push(y);
        }
        queue1 = queue2;
        queue2 = std::queue<int>();
    }

    int pop() {
        int val = queue1.front();
        queue1.pop();
        return val;
    }

    int top() {
        return queue1.front();
    }

    bool empty() {
        return queue1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
// @lc code=end

