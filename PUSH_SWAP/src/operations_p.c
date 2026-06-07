/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_p.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.com>#+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-21 13:28:31 by nocrespo          #+#    #+#             */
/*   Updated: 2026-01-21 13:28:31 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	push_stack(t_list **dst, t_list **src)
{
	t_list	*tmp;

	if (!src || !*src)
		return (0);
	tmp = *src;
	*src = tmp->next;
	tmp->next = *dst;
	*dst = tmp;
	return (1);
}

void	pa(t_list **dst, t_list **src, t_bench *bench)
{
	if (push_stack(dst, src) == 1)
	{
		write (1, "pa\n", 3);
		if (bench)
		{
			bench->ops.pa++;
			bench->total_ops++;
		}
	}
}

void	pb(t_list **dst, t_list **src, t_bench *bench)
{
	if (push_stack(dst, src) == 1)
	{
		write (1, "pb\n", 3);
		if (bench)
		{
			bench->ops.pb++;
			bench->total_ops++;
		}
	}
}
