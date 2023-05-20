import os
import sys
import unittest

"""
Python script to run all test files in this direcotry.
Run this file with 'python run.py' or test and modify indiviudal test files(recommended).
Update your python version if necesary and get testing.
"""

PYTHON_VERSION = 'python3.10'

def main():
    sys.path.append('../')

    test_files = os.listdir()

    test_files.remove('run.py')

    for file in test_files:
        print(f"Running {file}")
        os.system(f"{PYTHON_VERSION} {file}")

if __name__ == '__main__':
    main()