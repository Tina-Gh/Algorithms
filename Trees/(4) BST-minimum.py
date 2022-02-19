def min_value_node(self, current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node 