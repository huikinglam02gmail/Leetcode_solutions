/*
 * @lc app=leetcode id=1845 lang=cpp
 *
 * [1845] Seat Reservation Manager
 */

// @lc code=start
class SeatManager {
private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> free;

public:
    SeatManager(int n) {
        for (int i = 1; i <= n; ++i) {
            free.push(i);
        }
    }

    int reserve() {
        int seat = free.top();
        free.pop();
        return seat;
    }

    void unreserve(int seatNumber) {
        free.push(seatNumber);
    }
};


/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
// @lc code=end

