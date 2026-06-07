/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   count_args.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: chmorale <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 09:48:15 by chmorale          #+#    #+#             */
/*   Updated: 2026/01/25 09:48:27 by chmorale         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	count_items(char *str, int *count)
{
	int		i;
	int		valid_number;

	valid_number = 0;
	i = 0;
	while (str[i])
	{
		if ((str[i] == '-' || str[i] == '+') && (str[i + 1] < '0'
				|| str[i + 1] > '9'))
			return (0);
		else if ((str[i] >= '0' && str[i] <= '9') || str[i] == '-'
			|| str[i] == '+')
		{
			if (valid_number == 0 && ++(*count))
				valid_number = 1;
		}
		else if (str[i] == '\t' || str[i] == ' ')
			valid_number = 0;
		else
			return (0);
		i++;
	}
	return (1);
}

int	count_args(char **cur, t_flags *flags, int *count)
{
	char	*s;

	while (*cur)
	{
		s = *cur;
		if (check_flags(s, flags) == 1)
		{
			cur++;
			continue ;
		}
		if (!count_items(s, count))
			return (0);
		cur++;
	}
	return (1);
}
