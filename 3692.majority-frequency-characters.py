#
# @lc app=leetcode id=3692 lang=python3
#
# [3692] Majority Frequency Characters
#

# @lc code=start
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        group = {}
        for i, freq in enumerate(count):
            if freq > 0:
                if freq not in group:
                    group[freq] = []
                group[freq].append(chr(i + ord('a')))
        data = sorted(group.items(), key=lambda x: (-len(x[1]), - x[0]))
        return ''.join(sorted(data[0][1]))
# @lc code=end

