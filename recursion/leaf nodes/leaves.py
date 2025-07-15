from binary_tree import BinaryTree
from typing import Union, Tuple

def leaves(tree: Union[BinaryTree, None]) -> int: 
    '''
    Compute the total number of interesting leaf nodes. 
    You must only traverse through the tree once. 

    Arguments:
        tree: a binary tree with integer values

    Returns:
        The total number of interesting leaf nodes 
    '''
    # TODO: Write your solution here

    def helper(node: Union[BinaryTree, None], path_length: int, path_sum: int) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            if path_sum < path_length:
                return 1
            else:
                return 0

        new_length = path_length + 1
        new_sum = path_sum + node.value

        left_count = helper(node.left, new_length, new_sum)
        right_count = helper(node.right, new_length, new_sum)

        return left_count + right_count

    return helper(tree, 0, 0)

def mk_node(val: int,
            left: Union[BinaryTree, None],
            right: Union[BinaryTree, None]) -> BinaryTree:
    """
    Create a binary tree node, given the node number, value,
    left child, and right child.
    """
    t = BinaryTree(val)
    t.add_left(left)
    t.add_right(right)
    return t

def mk_sample_tree() -> BinaryTree:
    '''
    Make the sample tree from the problem statement.

    Returns:
        The root node of the sample tree
    '''
    return mk_node(-1,
               mk_node(15,
                   mk_node(20, None,None),
                   mk_node(-13, mk_node(7,None,None),None)),
               mk_node(10,None, None))

if __name__ == "__main__":
    tree = mk_sample_tree()
    print(leaves(tree))  # Output should be 2