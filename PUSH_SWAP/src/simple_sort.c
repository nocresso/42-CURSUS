/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.co  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 19:27:20 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/30 20:23:43 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	put_max_first(t_list **stack_a, int size, int min_pos,
				t_bench *bench)
{
	if (min_pos < size / 2)
	{
		while (min_pos > 0)
		{
			ra(stack_a, bench);
			min_pos--;
		}
	}
	else if (min_pos >= size / 2)
	{
		while (min_pos < size)
		{
			rra(stack_a, bench);
			min_pos++;
		}
	}
}

static void	restore_stack(t_list **stack_a, t_list **stack_b, t_bench *bench)
{
	if (!stack_b || !(*stack_b))
		return ;
	while ((*stack_b) != NULL)
		pa(stack_a, stack_b, bench);
}

void	simple_sort(t_list **stack_a, t_list **stack_b, int size,
		t_bench *bench)
{
	int	min_pos;

	if (size <= 5)
	{
		sort_small(stack_a, stack_b, size, bench);
		return ;
	}
	while (*stack_a != NULL)
	{
		min_pos = find_min(*stack_a);
		put_max_first(stack_a, size, min_pos, bench);
		pb(stack_b, stack_a, bench);
		size--;
	}
	restore_stack(stack_a, stack_b, bench);
}
