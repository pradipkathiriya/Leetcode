"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldTonew = {}

        def make_copy(node):

            if node in oldTonew:
                return oldTonew[node]

            new_node = Node(node.val)

            oldTonew[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(make_copy(nei))


            return new_node


        return make_copy(node) if node else None









        