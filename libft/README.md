
*This project was created as part of the 42 curriculum by nocrespo.*

**Description**

libft is a personal C library developed as part of the 42 School curriculum, it is the first project of the cursus.
The goal of this project is to reimplement a selection of standard C library functions, as well as additional utility functions, in order to gain a deeper understanding of how they work internally.
This library is intended to be reused in future C projects throughout the cursus.
The library includes functions grouped into three main categories:

1. Libc Functions Reimplementation: 

A set of standard C library functions reimplemented with the ft_ prefix. All functions follow the behavior described in their respective manual pages:

- Character checks (ft_isalpha, ft_isdigit, ...)

- String manipulation (ft_strlen, ft_strchr, ft_strncmp, ...)

- Memory manipulation (ft_memset, ft_memcpy, ft_memmove, ...)

- Conversion functions (ft_atoi)

- Memory allocation (ft_calloc, ft_strdup)

2. Additional Utility Functions:

Functions not included in the standard libc or implemented differently, such as:

- String creation and manipulation (ft_substr, ft_strjoin, ft_strtrim, ft_split)

- Integer to string conversion (ft_itoa)

- Functional string iteration (ft_strmapi, ft_striteri)

- Output functions using file descriptors (ft_putchar_fd, ft_putstr_fd, ft_putendl_fd, ft_putnbr_fd)

3. Linked List Functions:

A set of functions to manipulate singly linked lists. These functions allow creation, modification, and deletion of linked lists (ft_lstnew.c, ft_lstadd_front.c, ft_lstsize.c, ft_lstlast.c, ft_lstadd_back.c, ft_lstdelone.c, ft_lstclear.c, ft_lstiter.c, ft_lstmap.c).

**Instructions**

To compile the library, run: make
This will generate the libft.a static library at the root of the repository.
The Makefile supports the following rules:

- make or make all – compile the library

- make clean – remove object files

- make fclean – remove object files and the library

- make re – recompile the library from scratch

To use libft in another project:

Include the header file: #include "libft.h"

Compile your project with libft.a.

**Resources**

- Linux manual pages (man malloc, man strdup, etc)

- AI was used as a learning support in order to clarify theorethical concepts, better understanding of linked lists and review functions behavior when man pages were not clear. 


**Author**
nocrespo - 42Student



