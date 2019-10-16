class Solution:

    def get_first_occurrence(self, nums, target, start, end):
        if start == end and nums[start] != target:
            return -1

        mid = start + ((end - start) // 2)
        if nums[mid] == target:
            if nums[mid - 1] != target:
                return mid
            else:
                return self.get_first_occurrence(nums, target, start, mid - 1)
        elif nums[mid] > target:
            return self.get_first_occurrence(nums, target, start, mid - 1)
        elif nums[mid] < target:
            return self.get_first_occurrence(nums, target, mid + 1, end)

    def get_last_occurrence(self, nums, target, start, end):
        if start == end and nums[start] != target:
            return -1
        mid = start + ((end - start) // 2)
        if nums[mid] == target:
            if nums[mid + 1] != target:
                return mid
            else:
                return self.get_last_occurrence(nums, target, mid + 1, end)
        elif nums[mid] > target:
            return self.get_last_occurrence(nums, target, start, mid - 1)
        elif nums[mid] < target:
            return self.get_last_occurrence(nums, target, mid + 1, end)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        if nums[0] == target:
            first_occurrence = 0
        else:
            first_occurrence = self.get_first_occurrence(
                nums, target, 0, len(nums) - 1)

        if nums[-1] == target:
            last_occurrence = len(nums) - 1
        else:
            last_occurrence = self.get_last_occurrence(
                nums, target, 0, len(nums) - 1)

        return [first_occurrence, last_occurrence]


def main():
    solution = Solution()
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solution.searchRange([], 8) == [-1, -1]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 10) == [5, 5]
    assert solution.searchRange([2, 2], 1) == [-1, -1]


if __name__ == '__main__':
    main()
