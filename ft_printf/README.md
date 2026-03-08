
*This project was created as part of the 42 curriculum by nocrespo.*

**Description**

ft_printf is a partial reimplementation of the C standard library function printf.
The goal of this project is to learn how to work with variadic functions, format parsing, and type handling, without implementing the internal buffering system of the original printf.

The function prints directly to the standard output using write.

1. Implemented features

The ft_printf function supports the following format specifiers:

- %c: prints a single character

- %s: prints a string

- %d / %i: prints a signed integer

- %u: prints an unsigned integer

- %x: prints a lowercase hexadecimal number

- %X: prints an uppercase hexadecimal number

- %p: prints a memory adress

- %%: prints a percent sign

2. Return value

ft_printf returns the total number of characters printed.

The behavior mimics the original printf under normal execution conditions.

Error handling for write is not implemented, as it is not required by the subject. 

3. Special cases

- If a NULL pointer is passed to %s, the output is (null)

- If a NULL pointer is passed to %p, the output is (nil)

**Instructions**

1. Main files:

- ft_printf.c → main function and format parsing

- ft_printf_numbers.c → numeric formats (%d, %i, %u, %x, %X)

- ft_print_pointer.c → pointer handling (%p)

- ft_print_utils.c → helper functions (%c, %s, %%)

- ft_printf.h → header file

2. Compilation

To compile the library: make

This will generate the libftprintf.a static library at the root of the repository.
The Makefile supports the following rules:

- make or make all – compile the library

- make clean – remove object files

- make fclean – remove object files and the library

- make re – recompile the library from scratch

To use ft_printf in another project:

Include the header file: #include "ft_printf.h"

Compile your project with libftprintf.a.

**Resources**

- Linux manual pages (man 2 write, man 3 stdarg)

- Variadic functions YouTube tutorial.

- AI was used as a learning support in order to clarify theorethical concepts and better understanding of variadic functions.


**Author**
nocrespo - 42Student



