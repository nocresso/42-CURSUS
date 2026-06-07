/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: chmorale <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 14:27:07 by chmorale          #+#    #+#             */
/*   Updated: 2026/01/30 18:35:43 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_three(t_list **stack_a, t_bench *bench)
{
	int	max;
	int	min;

	min = get_min_index(*stack_a);
	max = get_max_index(*stack_a);
	if ((*stack_a)->index == max)
	{
		ra(stack_a, bench);
		if ((*stack_a)->index != min)
			sa(stack_a, bench);
	}
	else if ((*stack_a)->index == min)
	{
		sa(stack_a, bench);
		ra(stack_a, bench);
	}
	else
	{
		if ((*stack_a)->next->index == max)
			rra(stack_a, bench);
		else
			sa(stack_a, bench);
	}
}

void	sort_four(t_list **stack_a, t_list **stack_b, t_bench *bench)
{
	int	position;
	int	size;

	if (!stack_a || !*stack_a || ft_lstsize(*stack_a) != 4)
		return ;
	size = ft_lstsize(*stack_a);
	position = find_index_pos(*stack_a, 0);
	if (position <= (size / 2))
	{
		while (position-- > 0)
			ra(stack_a, bench);
	}
	else
	{
		position = size - position;
		while (position > 0)
		{
			rra(stack_a, bench);
			position--;
		}
	}
	pb(stack_b, stack_a, bench);
	sort_three(stack_a, bench);
	pa(stack_a, stack_b, bench);
}

void	sort_five(t_list **stack_a, t_list **stack_b, t_bench *bench)
{
	int		position;
	int		min;

	min = get_min_index(*stack_a);
	position = find_min(*stack_a);
	if (position <= (ft_lstsize(*stack_a) / 2))
		while ((*stack_a)->index != min)
			ra(stack_a, bench);
	else
		while ((*stack_a)->index != min)
			rra(stack_a, bench);
	pb(stack_b, stack_a, bench);
	min = get_min_index(*stack_a);
	position = find_min(*stack_a);
	if (position <= (ft_lstsize(*stack_a) / 2))
		while ((*stack_a)->index != min)
			ra(stack_a, bench);
	else
		while ((*stack_a)->index != min)
			rra(stack_a, bench);
	pb(stack_b, stack_a, bench);
	sort_three(stack_a, bench);
	pa(stack_a, stack_b, bench);
	pa(stack_a, stack_b, bench);
}

int	sort_small(t_list **stack_a, t_list **stack_b, int size, t_bench *bench)
{
	stack_index(*stack_a, size);
	if (size == 2)
		sa(stack_a, bench);
	else if (size == 3)
		sort_three(stack_a, bench);
	else if (size == 4)
		sort_four(stack_a, stack_b, bench);
	else if (size == 5)
		sort_five(stack_a, stack_b, bench);
	return (1);
}
