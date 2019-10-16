class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1
        while start < end:

            mid = start + ((end - start) // 2)
            # print("start: {}; mid: {}; end: {}".format(start, mid, end))
            if nums[mid] > nums[end]:
                if target > nums[mid] or target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid

        return start if start == end and target == nums[start] else -1


def main():
    solution = Solution()
    assert solution.search([], 0) == -1
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solution.search([1, 3], 3) == 1


if __name__ == '__main__':
    main()
