/*
 * @lc app=leetcode id=232 lang=cpp
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start
#include <stack>

class MyQueue {
private:
    std::stack<int> stack1;
    std::stack<int> stack2;

    void clearance() {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
    }

public:
    MyQueue() {}

    void push(int x) {
        stack1.push(x);
    }

    int pop() {
        clearance();
        int topElement = stack2.top();
        stack2.pop();
        return topElement;
    }

    int peek() {
        clearance();
        return stack2.top();
    }

    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};


/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end

