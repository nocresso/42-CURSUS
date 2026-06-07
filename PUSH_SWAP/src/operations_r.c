/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_r.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.com>#+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-21 13:28:31 by nocrespo          #+#    #+#             */
/*   Updated: 2026-01-21 13:28:31 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	rotate_stack(t_list **stack)
{
	t_list	*first;
	t_list	*last;

	if (!stack || !*stack || !(*stack)->next)
		return (0);
	first = *stack;
	*stack = first->next;
	first->next = NULL;
	last = *stack;
	while (last->next != NULL)
		last = last->next;
	last->next = first;
	return (1);
}

void	ra(t_list **stack, t_bench *bench)
{
	if (rotate_stack(stack) == 1)
	{
		write (1, "ra\n", 3);
		if (bench)
		{
			bench->ops.ra++;
			bench->total_ops++;
		}
	}
}

void	rb(t_list **stack, t_bench *bench)
{
	if (rotate_stack(stack) == 1)
	{
		write (1, "rb\n", 3);
		if (bench)
		{
			bench->ops.rb++;
			bench->total_ops++;
		}
	}
}

void	rr(t_list **stack1, t_list **stack2, t_bench *bench)
{
	int	success1;
	int	success2;

	success1 = rotate_stack(stack1);
	success2 = rotate_stack(stack2);
	if (success1 == 1 || success2 == 1)
	{
		write (1, "rr\n", 3);
		if (bench)
		{
			bench->ops.rr++;
			bench->total_ops++;
		}
	}
}
