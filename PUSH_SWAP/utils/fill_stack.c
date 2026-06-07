/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fill_stack.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 17:03:26 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/19 18:22:21 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_list	*fill_stack(int *num, int total)
{
	int		i;
	t_list	*new;
	t_list	*head;

	i = 0;
	head = new_node(num[i]);
	if (!head)
		return (NULL);
	i++;
	while (i < total)
	{
		new = new_node(num[i]);
		if (!new)
		{
			free_node(&head);
			return (NULL);
		}
		ft_lstadd_back(&head, new);
		i++;
	}
	return (head);
}
