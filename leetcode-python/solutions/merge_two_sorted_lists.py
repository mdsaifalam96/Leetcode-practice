# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        node_1 = l1
        node_2 = l2
        head_merged = ListNode(0)
        node_merged = head_merged

        while node_1 and node_2:
            if node_1.val < node_2.val:
                node_merged.next = node_1
                node_1 = node_1.next
            else:
                node_merged.next = node_2
                node_2 = node_2.next
            node_merged = node_merged.next

        if node_1:
            node_merged.next = node_1
        elif node_2:
            node_merged.next = node_2

        return head_merged.next


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
    assert get_list(
        solution.mergeTwoLists(
            get_nodes([]),get_nodes([])))  == []
    assert get_list(
        solution.mergeTwoLists(
            get_nodes([]),get_nodes([1, 2, 4])))  == [1, 2, 4]
    assert get_list(
        solution.mergeTwoLists(
            get_nodes([1, 2, 4]),get_nodes([])))  == [1, 2, 4]
    assert get_list(
        solution.mergeTwoLists(
            get_nodes([1, 2, 4]),get_nodes([1, 3, 4])))  == [1, 1, 2, 3, 4, 4]
    assert get_list(
        solution.mergeTwoLists(
            get_nodes([1, 2, 4, 5, 9]),get_nodes([1, 3, 10])))  == [1, 1, 2, 3, 4, 5, 9, 10]

if __name__ == '__main__':
    main()
