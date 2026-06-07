/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   chunks_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.co  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 16:51:57 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/30 20:00:24 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_sqrt(int nb)
{
	int	sq;

	sq = 1;
	if (nb <= 0)
		return (0);
	while (sq * sq < nb)
	{
		sq++;
	}
	if (sq * sq == nb)
		return (sq);
	else if (sq * sq > nb)
		return (sq - 1);
	return (0);
}

static int	find_max(t_list *stack)
{
	int		max;
	int		i;
	t_list	*current;
	t_list	*tmp;

	i = 0;
	if (!stack)
		return (-1);
	max = stack->index;
	tmp = stack;
	current = tmp->next;
	while (current)
	{
		if (max < current->index)
			max = current->index;
		current = current->next;
	}
	while (tmp)
	{
		if (tmp->index == max)
			return (i);
		tmp = tmp->next;
		i++;
	}
	return (-1);
}

static void	final_sort(t_list **stack_a, t_list **stack_b, int size,
			t_bench *bench)
{
	int	max_pos;

	while (*stack_b != NULL)
	{
		max_pos = find_max(*stack_b);
		if (max_pos < size / 2)
		{
			while (max_pos > 0)
			{
				rb(stack_b, bench);
				max_pos--;
			}
		}
		else if (max_pos >= size / 2)
		{
			max_pos = size - max_pos;
			while (max_pos > 0)
			{
				rrb(stack_b, bench);
				max_pos--;
			}
		}
		pa(stack_a, stack_b, bench);
		size--;
	}
}

void	chunks_sort(t_list **stack_a, t_list **stack_b, int size,
		t_bench *bench)
{
	int	chunks_num;
	int	i;
	int	chunk_size;
	int	size_b;

	chunks_num = ft_sqrt(size);
	chunk_size = chunks_num;
	size_b = size;
	while (*stack_a != NULL)
	{
		i = 0;
		while (i < chunk_size && size > 0)
		{
			if (stack_a && *stack_a && (*stack_a)->index < chunks_num)
			{
				pb(stack_b, stack_a, bench);
				i++;
				size--;
			}
			else
				ra(stack_a, bench);
		}
		chunks_num = chunks_num + chunk_size;
	}
	final_sort(stack_a, stack_b, size_b, bench);
}
