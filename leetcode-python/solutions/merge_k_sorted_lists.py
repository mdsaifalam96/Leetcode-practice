# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from heapq import heapify, heappop, heappush


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merged_head = ListNode(None)
        prev_node = merged_head
        appearances = dict()

        heap = list()
        for node in lists:
            if node:
                entry_count = 1
                if node.val in appearances:
                    entry_count = appearances[node.val] + 1
                appearances[node.val] = entry_count
                heap.append([node.val, entry_count, node])

        heapify(heap)

        while heap:
            current_smallest = heappop(heap)[-1]
            prev_node.next = current_smallest
            next_node = current_smallest.next
            if next_node:
                entry_count = 1
                if next_node.val in appearances:
                    entry_count = appearances[next_node.val] + 1
                appearances[next_node.val] = entry_count
                heappush(heap, [next_node.val, entry_count, next_node])
            prev_node = prev_node.next

        return merged_head.next


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
        solution.mergeKLists(
            [get_nodes([]), get_nodes([]), get_nodes([])])) == []
    assert get_list(
        solution.mergeKLists(
            [get_nodes([]), get_nodes([1, 2, 4])])) == [1, 2, 4]
    assert get_list(
        solution.mergeKLists(
            [get_nodes([1, 2, 4]), get_nodes([])])) == [1, 2, 4]
    assert get_list(
        solution.mergeKLists(
            [get_nodes([1, 2, 4]), get_nodes([1, 3, 4])])) == [1, 1, 2, 3, 4, 4]
    assert get_list(
        solution.mergeKLists(
            [get_nodes([1, 2, 4, 5, 9]), get_nodes([2, 3, 10])])) == [1, 2, 2, 3, 4, 5, 9, 10]
    assert get_list(
        solution.mergeKLists(
            [get_nodes([1, 2, 4, 5, 9]), get_nodes([2, 3, 10]), get_nodes([8, 9])])) == [1, 2, 2, 3, 4, 5, 8, 9, 9, 10]


if __name__ == '__main__':
    main()
