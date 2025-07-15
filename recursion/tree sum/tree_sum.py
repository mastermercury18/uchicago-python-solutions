from binary_tree import BinaryTree
from typing import Union, Tuple


def tree_sum(tree: Union[BinaryTree, None], ceiling: int) -> int:
    '''
    Compute the sum of all the values in the tree, up to the given
    ceiling (short-circuiting the traversal of the tree is we hit
    that ceiling)

    Arguments:
        tree: a binary tree with integer values
        ceiling: the maximum value for the sum of values

    Returns:
        The sum of all the values in the tree or, if that sum
        is greater than the ceiling value, return the ceiling
        value.
    '''
    # TODO: Write your solution here

    def helper(node: Union[BinaryTree, None], running_sum: int) -> Tuple[int, bool]:
        if node is None:
            return running_sum, False
        
        running_sum += node.value

        if running_sum >= ceiling:
            return ceiling, True

        left_sum, bool = helper(node.left, running_sum)
        if bool is True:
            return left_sum, True 
        
        right_sum, bool = helper(node.right, left_sum)
        return (right_sum, bool)
    
    final_sum, final_bool = helper(tree, 0)
    return final_sum


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
    return mk_node(10,
               mk_node(5,
                   None,
                   mk_node(15,
                           mk_node(5, None, None),
                           mk_node(10, None, None))),
               mk_node(20,
                   mk_node(5, None, None),
                   mk_node(5,
                           mk_node(15, None, None),
                           None)))