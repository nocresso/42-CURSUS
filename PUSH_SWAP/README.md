
**Description**

push_swap is an algorithmic project whose goal is to sort a list of integers using two stacks (a and b) and a restricted set of operations. The challenge is not only to sort the numbers correctly, but to do so using the smallest possible number of operations.

The project focuses on algorithmic complexity, decision-making based on input characteristics, and clean, well-structured C code that follows the 42 Norm.

1. Program Behavior

Only a limited set of stack operations is allowed:

- swap: sa, sb, ss

- push: pa, pb

- rotate: ra, rb, rr

- reverse rotate: rra, rrb, rrr

The program takes a list of integers as arguments, where the first argument represents the top of stack a. 

The output is a sequence of operations, each separated by a newline, that sorts the stack in ascending order.

If the input is already sorted, the program produces no output.

Error handling: In case of invalid input (non-integers, duplicates, overflow), the program prints Error followed by a newline to stderr.

The input can be provided as separated arguments and/or as strings, with numbers separated by spaces or tabs.

2. Disorder index

Before performing any operation, the program computes a disorder index, a value between 0 and 1 that represents how far the input stack is from being sorted.

The index is calculated by counting how many pairs of elements are out of order, divided by the total number of possible pairs.

This value is used to dynamically select the most appropriate sorting strategy for inputs larger than 5 elements.

3. Sorting strategies

This project implements multiple sorting strategies with different complexity classes. The chosen strategy depends on the level of disorder.

- **Simple Algorithm** — O(n²)

A basic sorting strategy based on the Selection sort algorithm used for inputs with a low disorder.

- **Intermediate Algorithm** — O(n√n)

A chunk-based strategy that divides the input into blocks.

- **Complex Algorithm** — O(n log n)

A radix-based sorting strategy used for highly disordered inputs.

- **Adaptive Strategy**

The default behavior of push_swap is adaptive:

- Inputs of size ≤ 5 are handled by the small sort.

Dedicated optimal solutions.

Time complexity: O(1)

Space complexity: O(1)

For larger inputs:

- Low disorder (disorder < 0.2) → O(n²)

Used for nearly sorted inputs.

Time complexity (Push_swap model): O(n²)

Space complexity: O(1)

- Medium disorder (0.2 ≤ disorder < 0.5) → O(n√n)

Divides the input into blocks to reduce unnecessary rotations.

Time complexity (Push_swap model): O(n√n)

Space complexity: O(n) (stack usage)

- High disorder (disorder ≥ 0.5) → O(n log n)

Used for highly disordered inputs and large datasets.

Time complexity (Push_swap model): O(n log n)

Space complexity: O(n)

This design ensures both correctness and efficiency while avoiding unnecessary algorithmic overhead.


**Instructions**

1. Compilation

To compile the project, run:

*make*

This will generate the push_swap executable.

Available Makefile rules:

*make*        # Compile the project
*make clean*  # Remove object files
*make fclean* # Remove object files and executable
*make re*     # Recompile the project

The project is compiled with the flags -Wall -Wextra -Werror.

2. Execution

The program expects a list of integers as arguments, as separated arguments or as strings.
Example:

./push_swap 3 2 1

The output is a list of operations (one per line) that sorts the stack in ascending order.

3. Strategy Selection

By default, the program runs in adaptive mode, automatically choosing the most appropriate algorithm.

Optional flags can be used to force a specific strategy:

--simple    # Force O(n²) strategy
--medium    # Force O(n√n) strategy
--complex   # Force O(n log n) strategy
--adaptive  # Force adaptive strategy (default)

Example:

./push_swap --complex 5 4 3 2 1

4. Checker Usage

The output of push_swap can be piped to a checker program to verify correctness:

ARG="3 2 1" ./push_swap $ARG | ./checker_linux $ARG

If the sequence of operations correctly sorts the stack, the checker prints OK.

5. Benchmark Mode

The optional benchmark mode prints performance metrics to stderr:

Benchmark information includes:

- Disorder index

- Strategy used and complexity class

- Total number of operations

- Operation count per instruction

**Authors**
chmorale and nocrespo - 42Student

