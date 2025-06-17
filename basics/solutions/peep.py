def peep(p, e):
    """
    Determine whether or not peep = pp^e
    Inputs:
      p (int): first digit
      e (int): second digit
    Returns: True if peep = pp^e, False otherwise
    """
    my_peep = int(str(p) + str(e) + str(e) + str(p))
    ppe = pow(int(str(p) + str(p)), e)
    if my_peep == ppe:
        return True 
    else:
        return False
    ### Replace pass with your code


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

def do_test_peep(p, e, expected):
    recreate_msg = utils.gen_recreate_msg("peep", *(p, e))

    actual = peep(p, e)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_peep_1():
    do_test_peep(p=1, e=3, expected=True)

def test_peep_2():
    do_test_peep(p=3, e=1, expected=False)

def test_peep_3():
    do_test_peep(p=0, e=1, expected=False)

def test_peep_4():
    do_test_peep(p=1, e=0, expected=False)

def test_peep_5():
    do_test_peep(p=1, e=2, expected=False)

def test_peep_6():
    do_test_peep(p=2, e=3, expected=False)

if __name__ == "__main__":
    test_peep_1()
    test_peep_2()
    test_peep_3()
    test_peep_4()
    test_peep_5()
    test_peep_6()
