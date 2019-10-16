import sys

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        # print("nums", nums)
        closest = None
        closest_sum = sys.maxsize

        i = 0
        while i < len(nums) - 2:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                num_sum = nums[i] + nums[j] + nums[k]
                target_sum = num_sum - target
                # print("i:{}; j:{}; k:{}".format(i, j, k))
                # print("target_sum: {}".format(target_sum))
                if target_sum == 0:
                    return target

                if abs(target_sum) < closest_sum:
                    closest_sum = abs(target_sum)
                    closest = num_sum
                    # print("closest is now {}; closest_sum is {}".format(closest, closest_sum))
                
                if target_sum < 0:
                    j += 1
                elif target_sum > 0:
                    k -= 1

            i += 1

        # print(closest)
        return closest


def main():
    solution = Solution()
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([-1, 0, 1, 2], 4) == 3
    assert solution.threeSumClosest([-1, 0, 2], 0) == 1
    assert solution.threeSumClosest([-1, 0, 2, -1, -4], -3) == -3
    assert solution.threeSumClosest([-2, 0, 1, 1, 2], -5) == -1
    assert solution.threeSumClosest([0, 2, 1, -3], 1) == 0

if __name__ == '__main__':
    main()
