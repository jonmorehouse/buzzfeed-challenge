import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.join(current_dir, "../")
sys.path.insert(0, base_dir)


# import all tests
import signup_test



