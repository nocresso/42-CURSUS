/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_array.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: chmorale <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 17:16:39 by chmorale          #+#    #+#             */
/*   Updated: 2026/01/30 19:40:47 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	create_array(char *str, int *array, int *count)
{
	long	val;

	val = ft_atol(str);
	if (val > INT_MAX || val < INT_MIN)
		return (0);
	array[*count] = (int)val;
	(*count)++;
	return (1);
}
