/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: chmorale <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 09:31:01 by chmorale          #+#    #+#             */
/*   Updated: 2026/01/17 14:34:03 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	exit_error(int *array)
{
	if (array)
		free(array);
	write(2, "Error\n", 6);
	return (0);
}

static void	init_structs(t_flags *f, t_bench *b)
{
	f->method = -1;
	f->benchmark = -1;
	b->disorder = 0;
	b->strategy = NULL;
	b->total_ops = 0;
	b->ops.sa = 0;
	b->ops.sb = 0;
	b->ops.ss = 0;
	b->ops.pa = 0;
	b->ops.pb = 0;
	b->ops.ra = 0;
	b->ops.rb = 0;
	b->ops.rr = 0;
	b->ops.rra = 0;
	b->ops.rrb = 0;
	b->ops.rrr = 0;
}

int	process_items(char **str, t_flags *flags, int *array, int *count)
{
	int	i;
	int	res;

	i = 0;
	while (str[i])
	{
		res = check_flags(str[i], flags);
		if (res == -1)
			return (0);
		if (res == 1)
		{
			i++;
			continue ;
		}
		if (!valid_number(str[i]) || !create_array(str[i], array, count))
			return (0);
		i++;
	}
	return (1);
}

int	validations(char **cur, t_flags *flags, int *array, int *count)
{
	char	**item;

	while (*cur)
	{
		item = ft_split_tab(*cur, ' ', '\t');
		if (!item)
			return (0);
		if (!process_items(item, flags, array, count))
		{
			free_array(item);
			return (0);
		}
		free_array(item);
		cur++;
	}
	return (1);
}

int	main(int argc, char **argv)
{
	int		*int_array;
	int		count;
	t_flags	flags;
	t_list	*stack_a;
	t_bench	bench;

	if (argc < 2)
		return (0);
	count = 0;
	init_structs(&flags, &bench);
	if (!count_args(argv + 1, &flags, &count))
		return (exit_error(NULL));
	int_array = malloc(sizeof(int) * count);
	count = 0;
	init_structs(&flags, &bench);
	if (!int_array || !validations(argv + 1, &flags, int_array, &count)
		|| (!dup_valid(int_array, count)))
		return (exit_error(NULL));
	stack_a = fill_stack(int_array, count);
	free(int_array);
	if (!stack_a)
		return (exit_error(NULL));
	alg_selection(&stack_a, &flags, &bench);
	free_node(&stack_a);
	return (0);
}
