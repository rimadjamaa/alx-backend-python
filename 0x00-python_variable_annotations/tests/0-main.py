#!/usr/bin/env python3
import sys
import os

# Add parent directory (0x00-python) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the 'add' function from 0-add.py
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
