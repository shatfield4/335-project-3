# Soccer Opponent Avoidance Comparison

This project contains two algorithms for finding the number of possible paths in a soccer field grid, avoiding obstacles and opponents. The algorithms are implemented in Python and are compared using empirical analysis.

## Members

- Trenton Coggeshall (trenton.coggeshall@csu.fullerton.edu)
- Sean Hatfield (shatfield4@csu.fullerton.edu)
- Malik Hidouk (mhidouk@csu.fullerton.edu)

## Files

- `dynamic_programming.py`: Contains the `soccer_dyn_prog` function, which implements a dynamic programming algorithm to find the number of possible paths in the grid.
- `exhaustive_search.py`: Contains the `soccer_opponent_avoidance` function, which implements an exhaustive search algorithm to find the number of possible paths in the grid.
- `timing_comparisons.py`: A script that compares the two algorithms by running them on random test inputs of varying sizes and recording the execution times.

## How to Run

1. Make sure you have Python 3 installed on your system.

2. Clone or download this repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory containing the project files.

4. Run the `timing_comparisons.py` script by executing the following command:
``python timing_comparisons.py`` or you can run each algorithm individually by running ``python exhaustive_search.py`` or ``python dynamic_programming.py``

This will run both algorithms on random test inputs of varying sizes (defined in the `input_sizes` list) and print the execution times for each algorithm.

## Output

The output will show the timing data for both algorithms as lists of execution times. Each value corresponds to the execution time for a specific input size, in the same order as the `input_sizes` list.

Example output:

- ``Dynamic Programming Timings: [2.4416949599981308e-05, 2.9791961424052715e-05, 2.729194238781929e-05, 3.324996214359999e-05, 3.5541015677154064e-05, 4.033301956951618e-05, 5.141599103808403e-05]``

- ``Exhaustive Search Timings: [0.1333301670383662, 0.6154525829479098, 1.8384431669255719, 12.27649683400523, 46.746501999907196, 201.4424116659211, 971.6087485420285]``
