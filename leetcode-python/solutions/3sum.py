class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        # "sorted: {}".format(nums) == 

        i = 0
        solutions = list()
        while i < len(nums) - 2:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    solutions.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

            i += 1

        return solutions


def main():
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum([-1, 0, 1, 2]) == [[-1, 0, 1]]
    assert solution.threeSum([-1, 0, 2]) == []
    assert solution.threeSum([-1, 0, 2, -1, -4]) == [[-1, -1, 2]]
    assert solution.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]

if __name__ == '__main__':
    main()
