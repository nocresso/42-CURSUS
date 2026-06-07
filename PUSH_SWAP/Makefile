# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nocrespo <nocrespo@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 18:56:16 by nocrespo          #+#    #+#              #
#    Updated: 2026/01/30 20:30:43 by nocrespo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror -Iincludes

SRC_DIR = src/
UTILS_DIR = utils/

SRC = $(SRC_DIR)push_swap.c $(SRC_DIR)alg_strategy.c $(SRC_DIR)chunks_sort.c \
      $(SRC_DIR)operations_p.c $(SRC_DIR)operations_r.c $(SRC_DIR)operations_rr.c \
      $(SRC_DIR)operations_s.c $(SRC_DIR)radix_sort.c $(SRC_DIR)simple_sort.c \
      $(SRC_DIR)sort_small.c $(SRC_DIR)stack_index.c $(SRC_DIR)print_bench.c\
      $(UTILS_DIR)check_flags.c $(UTILS_DIR)count_args.c $(UTILS_DIR)create_array.c \
      $(UTILS_DIR)duplic_valid.c $(UTILS_DIR)fill_stack.c $(UTILS_DIR)find_min.c \
      $(UTILS_DIR)index_order.c $(UTILS_DIR)ft_strstr.c $(UTILS_DIR)ft_strchr.c \
      $(UTILS_DIR)free_array.c $(UTILS_DIR)free_node.c $(UTILS_DIR)ft_atol.c \
      $(UTILS_DIR)ft_lstadd_back.c $(UTILS_DIR)ft_lstsize.c $(UTILS_DIR)new_node.c \
      $(UTILS_DIR)valid_number.c $(UTILS_DIR)ft_strlen.c $(UTILS_DIR)ft_strlcpy.c \
      $(UTILS_DIR)ft_strcmp.c $(UTILS_DIR)ft_split_tab.c $(UTILS_DIR)ft_putnbr_fd.c\
      $(UTILS_DIR)movements_utils.c $(UTILS_DIR)ft_putstr_fd.c

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

%.o: %.c Makefile
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
