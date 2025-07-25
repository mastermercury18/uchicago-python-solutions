def num_divisible(lb, ub, p, q):
    """
    How many numbers between lb and ub (inclusive) are divisible by p
    or divisible by q, but not divisible by both p and q.
    """

    ### YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = 0
    for num in range(lb, ub+1):
        if not (num % p == 0 and num % q == 0):
            if num % p == 0:
                n += 1 
            elif num % q == 0:
                n += 1 
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n 


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import test_utils as utils

def do_test_num_divisible(lb, ub, p, q, expected):
    recreate_msg = utils.gen_recreate_msg("num_divisible", *(lb, ub, p, q))

    actual = num_divisible(lb, ub, p, q)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_num_divisible_1():
    do_test_num_divisible(lb=1, ub=20, p=2, q=3, expected=10)


def test_num_divisible_2():
    do_test_num_divisible(lb=2, ub=3, p=2, q=3, expected=2)


def test_num_divisible_3():
    do_test_num_divisible(lb=12, ub=20, p=2, q=2, expected=0)


def test_num_divisible_4():
    do_test_num_divisible(lb=1, ub=25, p=3, q=5, expected=11)


def test_num_divisible_5():
    do_test_num_divisible(lb=1, ub=25, p=27, q=5, expected=5)


def test_num_divisible_6():
    do_test_num_divisible(lb=1, ub=25, p=27, q=29, expected=0)

if __name__ == "__main__":
    test_num_divisible_1()
    test_num_divisible_2()
    test_num_divisible_3()
    test_num_divisible_4()
    test_num_divisible_5()
    test_num_divisible_6()
