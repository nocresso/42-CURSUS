/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_rr.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.com>#+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-21 13:28:31 by nocrespo          #+#    #+#             */
/*   Updated: 2026-01-21 13:28:31 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	reverse_rotate_stack(t_list **stack)
{
	t_list	*first;
	t_list	*tmp;
	t_list	*last;

	if (!stack || !*stack || !(*stack)->next)
		return (0);
	first = *stack;
	last = *stack;
	while (last->next->next != NULL)
		last = last->next;
	tmp = last->next;
	last->next = NULL;
	tmp->next = first;
	*stack = tmp;
	return (1);
}

void	rra(t_list **stack, t_bench *bench)
{
	if (reverse_rotate_stack(stack) == 1)
	{
		write (1, "rra\n", 4);
		if (bench)
		{
			bench->ops.rra++;
			bench->total_ops++;
		}
	}
}

void	rrb(t_list **stack, t_bench *bench)
{
	if (reverse_rotate_stack(stack) == 1)
	{
		write (1, "rrb\n", 4);
		if (bench)
		{
			bench->ops.rrb++;
			bench->total_ops++;
		}
	}
}

void	rrr(t_list **stack1, t_list **stack2, t_bench *bench)
{
	int	success1;
	int	success2;

	success1 = reverse_rotate_stack(stack1);
	success2 = reverse_rotate_stack(stack2);
	if (success1 == 1 || success2 == 1)
	{
		write (1, "rrr\n", 4);
		if (bench)
		{
			bench->ops.rrr++;
			bench->total_ops++;
		}
	}
}
