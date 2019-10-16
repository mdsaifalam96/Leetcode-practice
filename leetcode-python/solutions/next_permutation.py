class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return

        for index in range(len(nums) - 1, -1, -1):
            if index > 0 and nums[index - 1] < nums[index]:
                break

        # print(nums[index - 1], nums[index:])

        if index == 0:
            nums.reverse()
        else:
            for k in range(len(nums) - 1, index - 1, -1):
                if nums[k] > nums[index - 1]:
                    tmp = nums[k]
                    nums[k] = nums[index - 1]
                    nums[index - 1] = tmp
                    break

            sublist = nums[index:]
            sublist.reverse()
            nums[index:] = sublist
        # print(nums)


def main():
    solution = Solution()
    solution.nextPermutation([1, 2, 3])
    solution.nextPermutation([1, 1, 5])
    solution.nextPermutation([3, 2, 1])
    solution.nextPermutation([1, 3, 2])
    solution.nextPermutation([1, 3, 2, 7, 6, 4, 3, 2, 1])


if __name__ == '__main__':
    main()
