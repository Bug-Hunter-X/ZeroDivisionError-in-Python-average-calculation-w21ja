# ZeroDivisionError in Python Average Calculation

This repository demonstrates a common Python error: `ZeroDivisionError`.  The `bug.py` file contains code that attempts to calculate the average of an empty list, resulting in a division by zero.  The `bugSolution.py` file provides a corrected version that handles this edge case gracefully.

## How to reproduce the bug

1. Clone this repository.
2. Run `bug.py`.  You should see a `ZeroDivisionError`. 

## Solution

The solution involves checking if the input list is empty before performing the calculation.  See `bugSolution.py` for the corrected code.