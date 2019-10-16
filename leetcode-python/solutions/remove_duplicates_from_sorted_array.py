class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        elif nums[0] == nums[len(nums) - 1]:
            return 1

        last_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[last_index]:
                last_index += 1
                nums[last_index] = nums[i]

        return last_index + 1


def main():
    solution = Solution()
    assert solution.removeDuplicates([]) == 0
    assert solution.removeDuplicates([1, 1, 1]) == 1
    assert solution.removeDuplicates([1, 1, 2, 2, 2, 2, 2, 2]) == 2
    assert solution.removeDuplicates([1, 1, 2, 3, 3]) == 3
    assert solution.removeDuplicates([0, 1, 1, 2, 3, 4, 4]) == 5
    assert solution.removeDuplicates([0, 0, 0, 0, 3]) == 2


if __name__ == '__main__':
    main()
