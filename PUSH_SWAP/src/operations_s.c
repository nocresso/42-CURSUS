/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_s.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.com>#+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-21 13:28:31 by nocrespo          #+#    #+#             */
/*   Updated: 2026-01-21 13:28:31 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	swap_stack(t_list **stack)
{
	t_list	*first;
	t_list	*tmp;

	if (!stack || !*stack || !(*stack)->next)
		return (0);
	first = *stack;
	tmp = (*stack)->next;
	(*stack)->next = tmp->next;
	tmp->next = first;
	*stack = tmp;
	return (1);
}

void	sa(t_list **stack, t_bench *bench)
{
	if (swap_stack(stack) == 1)
	{
		write (1, "sa\n", 3);
		if (bench)
		{
			bench->ops.sa++;
			bench->total_ops++;
		}
	}
}

void	sb(t_list **stack, t_bench *bench)
{
	if (swap_stack(stack) == 1)
	{
		write (1, "sb\n", 3);
		if (bench)
		{
			bench->ops.sb++;
			bench->total_ops++;
		}
	}
}

void	ss(t_list **stack1, t_list **stack2, t_bench *bench)
{
	int	success1;
	int	success2;

	success1 = swap_stack(stack1);
	success2 = swap_stack(stack2);
	if (success1 == 1 || success2 == 1)
	{
		write (1, "ss\n", 3);
		if (bench)
		{
			bench->ops.ss++;
			bench->total_ops++;
		}
	}
}
