#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start


class Solution:
    # Max difference possible:
    # From left, scan for the first digit not equal to 9, starting from the first digit.
    # Turn all subsequent occurrence of that to be 9
    # If first digit is not equal to 1, turn all occurrence of it and afterwards to be 1
    # If first digit is equal to 1, From left, scan for the first digit not equal to 0, starting from the first digit.
    # Turn all subsequent occurrence of that to be 0
    
    def array_scanning(self, arr, default, start_index, forbidden):
        result, digit, found, n = [], default, False, len(arr)
        if start_index > 0:
            result += [arr[i] for i in range(start_index)]
        for i in range(start_index, n):
            if arr[i] != forbidden:
                if found and arr[i] == digit:
                    result.append(default)
                elif not found and arr[i] != default:
                    found = True
                    digit = arr[i]
                    result.append(default)
                else:
                    result.append(arr[i])
            else:
                result.append(arr[i])
        return int(''.join([str(x) for x in result]))

    def maxDiff(self, num: int) -> int:
        num_digits = [int(c) for c in str(num)]
        a = self.array_scanning(num_digits, 9, 0, 10)
        if num_digits[0] != 1:
            b = self.array_scanning(num_digits, 1, 0, 10)
        else:
            b = self.array_scanning(num_digits, 0, 1, 1)
        return a - b
                
# @lc code=end

