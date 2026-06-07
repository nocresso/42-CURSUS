/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   find_min.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.co  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 19:03:48 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/26 19:26:35 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	find_min(t_list *stack)
{
	int		min;
	int		i;
	t_list	*current;
	t_list	*tmp;

	i = 0;
	if (!stack)
		return (-1);
	min = stack->index;
	tmp = stack;
	current = tmp->next;
	while (current)
	{
		if (min > current->index)
			min = current->index;
		current = current->next;
	}
	while (tmp)
	{
		if (tmp->index == min)
			return (i);
		tmp = tmp->next;
		i++;
	}
	return (-1);
}
