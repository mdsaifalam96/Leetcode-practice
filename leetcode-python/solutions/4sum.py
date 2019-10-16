class Solution:

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        i = 0
        solutions = list()
        while i < len(nums) - 2:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                summed_up = nums[i] + nums[j] + nums[k]
                if summed_up == target:
                    solutions.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif summed_up < target:
                    j += 1
                elif summed_up > target:
                    k -= 1

            i += 1

        return solutions

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        solutions = list()
        i = 0
        while i < len(nums) - 3:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            target_for_3sum = target - nums[i]
            solutions_3sum = self.threeSum(nums[i + 1:], target_for_3sum)
            for solution in solutions_3sum:
                solutions.append([nums[i]] + solution)
            i += 1

        return solutions


def main():
    solution = Solution()
    assert solution.fourSum([1, 0, -1], 0) == []
    assert solution.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert solution.fourSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 13) == [[1, 2, 3, 7], [1, 2, 4, 6], [1, 3, 4, 5]]

if __name__ == '__main__':
    main()
