/*
 * @lc app=leetcode id=2069 lang=cpp
 *
 * [2069] Walking Robot Simulation II
 */

// @lc code=start
#include <vector>
#include <string>

class Robot {
private:
    int w, h, x, y, dir;
    bool walked;
    std::vector<std::vector<int>> dirs;
    std::vector<std::string> dirNames;

public:
    Robot(int width, int height) : w(width), h(height), x(0), y(0), dir(0), walked(false),
                                    dirs({{1, 0}, {0, 1}, {-1, 0}, {0, -1}}),
                                    dirNames({"East", "North", "West", "South"}) {}

    void step(int num) {
        num %= 2 * (w + h - 2);
        walked = true;
        for (int i = 0; i < num; i++) {
            if (!(0 <= x + dirs[dir][0] && x + dirs[dir][0] < w && 0 <= y + dirs[dir][1] && y + dirs[dir][1] < h)) {
                dir = (dir + 1) % 4;
            }
            x += dirs[dir][0];
            y += dirs[dir][1];
        }
    }

    std::vector<int> getPos() {
        return {x, y};
    }

    std::string getDir() {
        if (x == 0 && y == 0) {
            return walked ? "South" : "East";
        } else {
            return dirNames[dir];
        }
    }
};


/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
// @lc code=end

