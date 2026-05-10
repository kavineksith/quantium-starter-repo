#!/bin/bash

# activate virtual environment
source venv/bin/activate

# run tests
python -m pytest test_pink_morsel_visualizer.py
exit_code=$?

# return result to CI system
exit $exit_code