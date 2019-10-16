class Solution:
    def binary_search(self, nums, target, start, end):
        mid = start + ((end - start) // 2)

        if target == nums[mid] or target > nums[mid - 1] and target <= nums[mid]:
            return mid
        elif target > nums[mid] and target <= nums[mid + 1]:
            return mid + 1
        elif nums[mid] > target:
            return self.binary_search(nums, target, start, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, end)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        location = self.binary_search(nums, target, 0, len(nums) - 1)
        return location


def main():
    solution = Solution()
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0
    assert solution.searchInsert([1, 3], 3) == 1


if __name__ == '__main__':
    main()
