/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 11:23:17 by nocrespo          #+#    #+#             */
/*   Updated: 2026/02/02 17:39:42 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <limits.h>
# include <stdlib.h>
# include <unistd.h>
# include <stdio.h>

typedef struct s_list
{
	int				value;
	struct s_list	*next;
	int				index;
}	t_list;

typedef struct s_flags
{
	int	method;
	int	benchmark;
}	t_flags;

typedef struct s_ops
{
	int	sa;
	int	sb;
	int	ss;
	int	pa;
	int	pb;
	int	ra;
	int	rb;
	int	rr;
	int	rra;
	int	rrb;
	int	rrr;
}	t_ops;

typedef struct s_bench
{
	float	disorder;
	char	*strategy;
	int		total_ops;
	t_ops	ops;
}	t_bench;

long int	ft_atol(char *str);
char		*ft_strchr(const char *s, int c);
char		*ft_strstr(const char *s1, const char *s2);
int			ft_strcmp(const char *s1, const char *s2);
int			process_items(char **str, t_flags *flags, int *array, int *count);
int			validations(char **cur, t_flags *flags, int *array, int *count);
void		sort_three(t_list **stack_a, t_bench *bench);
void		sort_four(t_list **stack_a, t_list **stack_b, t_bench *bench);
void		sort_five(t_list **stack_a, t_list **stack_b, t_bench *bench);
int			sort_small(t_list **stack_a, t_list **stack_b, int size,
				t_bench *bench);
int			adaptative_sort(t_list **stack_a, t_list **stack_b, int size,
				t_bench *bench);
void		simple_sort(t_list **stack_a, t_list **stack_b, int size,
				t_bench *bench);
char		**ft_split_tab(char const *s, char c, char c2);
size_t		ft_strlen(const char *str);
size_t		ft_strlcpy(char *dst, const char *src, size_t size);
void		ft_lstadd_front(t_list **lst, t_list *new);
int			push_stack(t_list **dst, t_list **src);
void		pa(t_list **dst, t_list **src, t_bench *bench);
void		pb(t_list **dst, t_list **src, t_bench *bench);
int			rotate_stack(t_list **stack);
void		ra(t_list **stack, t_bench *bench);
void		rb(t_list **stack, t_bench *bench);
void		rr(t_list **stack1, t_list **stack2, t_bench *bench);
int			reverse_rotate_stack(t_list **stack);
void		rra(t_list **stack, t_bench *bench);
void		rrb(t_list **stack, t_bench *bench);
void		rrr(t_list **stack1, t_list **stack2, t_bench *bench);
int			swap_stack(t_list **stack);
void		sa(t_list **stack, t_bench *bench);
void		sb(t_list **stack, t_bench *bench);
void		ss(t_list **stack1, t_list **stack2, t_bench *bench);
float		index_order(t_list **lst);
void		stack_index(t_list *stack, int size);
void		free_node(t_list **lst);
void		ft_lstadd_back(t_list **lst, t_list *new);
t_list		*new_node(int value);
int			alg_selection(t_list **stack_a, t_flags *flags, t_bench *bench);
int			create_array(char *str, int *array, int *count);
void		free_array(char **array);
int			dup_valid(int *array, int count);
int			valid_number(char *str);
int			check_flags(char *str, t_flags *flags);
int			count_args(char **cur, t_flags *flags, int *count);
int			*ft_fill_array(char **str, int num_digits);
t_list		*fill_stack(int *num, int total);
int			find_min(t_list *stack);
void		radix_sort(t_list **stack_a, t_list **stack_b, int size,
				t_bench *bench);
int			find_index_pos(t_list *stack, int target_index);
int			get_max_index(t_list *stack);
int			get_min_index(t_list *stack);
void		chunks_sort(t_list **stack_a, t_list **stack_b, int size,
				t_bench *bench);
void		ft_putstr_fd(char *s, int fd);
int			ft_lstsize(t_list *lst);
void		ft_putnbr_fd(int n, int fd);
void		print_bench(t_flags *flags, t_bench *bench);

#endif
