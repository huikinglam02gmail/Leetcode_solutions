/*
 * @lc app=leetcode id=1845 lang=csharp
 *
 * [1845] Seat Reservation Manager
 */

// @lc code=start
public class SeatManager {

    PriorityQueue<int, int> free;
    public SeatManager(int n) {
        free = new PriorityQueue<int, int>();
        for (int i = 1; i <= n; ++i)
        {
            free.Enqueue(i, i);
        }    
    }
    
    public int Reserve() {
        return free.Dequeue();
    }
    
    public void Unreserve(int seatNumber) {
        free.Enqueue(seatNumber, seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
// @lc code=end

