/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_index.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.co  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 18:19:00 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/26 19:04:39 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	stack_index(t_list *stack, int size)
{
	t_list	*current;
	t_list	*tmp;
	t_list	*min;
	int		index;

	index = 0;
	while (index < size)
	{
		tmp = stack;
		while (tmp && tmp->index != -1)
			tmp = tmp->next;
		if (!tmp)
			break ;
		min = tmp;
		current = tmp->next;
		while (current)
		{
			if ((current->index == -1 && min->value > current->value))
				min = current;
			current = current->next;
		}
		min->index = index;
		index++;
	}
}
