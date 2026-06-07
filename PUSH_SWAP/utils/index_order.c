/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index_order.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: chmorale <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 11:38:14 by chmorale          #+#    #+#             */
/*   Updated: 2026/01/20 11:41:22 by chmorale         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

float	index_order(t_list **lst)
{
	float	order_i;
	int		total;
	t_list	*tmp;

	order_i = 0;
	total = 0;
	if (!lst)
		return (0);
	tmp = *lst;
	while (tmp->next != NULL)
	{
		if (tmp->value > tmp->next->value)
			order_i++;
		total++;
		tmp = tmp->next;
	}
	if (total != 0)
		order_i = (order_i / total);
	return (order_i);
}
