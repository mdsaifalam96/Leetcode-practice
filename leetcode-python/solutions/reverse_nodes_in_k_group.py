# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not k:
            return head

        def reverse_node_order(head):
            tail = head
            new_head = head
            current_node = head.next
            while current_node:
                next_node = current_node.next
                current_node.next = new_head
                new_head = current_node
                current_node = next_node

            return new_head, tail

        if not head or not head.next:
            return head

        current_node = head

        for _ in range(k - 1):
            if not current_node.next:
                return head
            current_node = current_node.next

        reversed_remaining = self.reverseKGroup(current_node.next, k)
        current_node.next = None
        new_head, tail = reverse_node_order(head)
        tail.next = reversed_remaining

        return new_head


def main():

    def get_nodes(values):
        next_node = None
        for value in values[::-1]:
            node = ListNode(value)
            node.next = next_node
            next_node = node

        return next_node

    def get_list(head):
        node = head
        nodes = list()
        while node:
            nodes.append(node.val)
            node = node.next
        return nodes

    solution = Solution()
    assert get_list(solution.reverseKGroup(get_nodes([]), 2)) == []
    assert get_list(solution.reverseKGroup(get_nodes([1]), 2)) == [1]
    assert get_list(solution.reverseKGroup(
        get_nodes([1, 2, 3, 4]), 2)) == [2, 1, 4, 3]
    assert get_list(solution.reverseKGroup(
        get_nodes([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert get_list(solution.reverseKGroup(
        get_nodes([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert get_list(solution.reverseKGroup(
        get_nodes([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
