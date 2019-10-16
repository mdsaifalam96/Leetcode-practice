''' Add Two Numbers '''

class ListNode:
    ''' Definition for singly-linked list '''
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        current_node = self
        constructed_string = ""
        while current_node:
            constructed_string += str(current_node.val) + " -> "
            current_node = current_node.next
        return constructed_string

    @staticmethod
    def create_linked_list(nums):
        ''' Creates a linked list from a regular list '''
        head = None
        nums.reverse()
        for _, num in enumerate(nums):
            node = ListNode(num)
            node.next = head
            head = node
        return head

class Solution:
    ''' Solution class '''

    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        current_l1_node = l1
        current_l2_node = l2
        carry_over = 0
        result_current_node = None
        result_prev_node = None
        result_head = None
        while current_l1_node or current_l2_node:
            current_sum = carry_over
            current_sum += current_l1_node.val if current_l1_node else 0
            current_sum += current_l2_node.val if current_l2_node else 0

            digit = current_sum % 10
            carry_over = 1 if current_sum > 9 else 0

            result_current_node = ListNode(digit)
            if result_prev_node:
                result_prev_node.next = result_current_node
            else:
                result_head = result_current_node
            result_prev_node = result_current_node

            current_l1_node = current_l1_node.next if current_l1_node else None
            current_l2_node = current_l2_node.next if current_l2_node else None

        if carry_over:
            result_current_node = ListNode(carry_over)
            result_prev_node.next = result_current_node

        return result_head


def main():
    ''' Main function '''
    solution = Solution()
    list1 = ListNode.create_linked_list([9, 9])
    list2 = ListNode.create_linked_list([1])
    print(solution.addTwoNumbers(list1, list2))

if __name__ == '__main__':
    main()
