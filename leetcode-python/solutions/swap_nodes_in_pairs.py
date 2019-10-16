# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swap_positions(self, prev_node, node_1, node_2):
        next_node = node_2.next
        prev_node.next = node_2
        node_2.next = node_1
        node_1.next = next_node

        return node_1

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        dummy_head = ListNode(None)
        dummy_head.next = head
        current_node = dummy_head

        while current_node.next and current_node.next.next:
            current_node = self.swap_positions(
                current_node, current_node.next, current_node.next.next)

        return dummy_head.next


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
    assert get_list(solution.swapPairs(get_nodes([]))) == []
    assert get_list(solution.swapPairs(get_nodes([1]))) == [1]
    assert get_list(solution.swapPairs(
        get_nodes([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert get_list(solution.swapPairs(
        get_nodes([1, 2, 3, 4, 5]))) == [2, 1, 4, 3, 5]


if __name__ == '__main__':
    main()
