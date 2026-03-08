*This project has been created as part of the 42 curriculum by nocrespo.*

# get\_next\_line

**Description**

The **get_next_line** project consists of implementing a function in C capable of reading from a file descriptor **line by line**, returning a complete line on each call, including the newline character (`\n`) when present.

The main goal of this project is to deepen the understanding of memory management in C, including dynamic allocation, the behavior of the `read` system call, the use of `static` variables, and correct handling of consecutive function calls without losing data.

In the **bonus** part, the function must handle **multiple file descriptors simultaneously**, maintaining an independent state for each one. This is achieved by maintaining an array of static buffers indexed by file descriptor, ensuring that each descriptor retains its own independent reading state.

---

**Instructions**


To compile the base version of the project:

cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 \
get_next_line.c get_next_line_utils.c

To compile the bonus version:

cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 \
get_next_line_bonus.c get_next_line_utils_bonus.c

**Resources**

- Manual pages: man 2 read, man 3 malloc, man 3 free
- Use of AI: AI was used as learning during the development of this project, for example to clarify concepts related to memory maangement and pointers and reason about edge cases and error escenarios.

**Author**
nocrespso - 42student

