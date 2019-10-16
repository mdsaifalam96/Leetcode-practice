# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        none_hunter = head
        n_prev_hunter = head

        for _ in range(n + 1):
            if not none_hunter:
                return head.next
            none_hunter = none_hunter.next
        # print(none_hunter)

        while none_hunter:
            none_hunter = none_hunter.next
            n_prev_hunter = n_prev_hunter.next
        # print(n_prev_hunter)
        n_prev_hunter.next = n_prev_hunter.next.next

        return head


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
    assert get_list(solution.removeNthFromEnd(get_nodes([0]), 1)) == []
    assert get_list(solution.removeNthFromEnd(get_nodes([0, 1]), 2)) == [1]
    assert get_list(solution.removeNthFromEnd(get_nodes([0, 1, 2, 3, 4]), 2)) == [0, 1, 2, 4] 
    assert get_list(solution.removeNthFromEnd(get_nodes([0, 1, 2, 3, 4]), 5)) == [1, 2, 3, 4]

if __name__ == '__main__':
    main()
