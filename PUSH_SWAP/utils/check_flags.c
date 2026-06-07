/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_flags.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: chmorale <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/24 09:53:41 by chmorale          #+#    #+#             */
/*   Updated: 2026/01/25 10:13:31 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	check_flags(char *str, t_flags *flags)
{
	char	*flags_source[4];
	int		i;

	flags_source[0] = "--simple";
	flags_source[1] = "--medium";
	flags_source[2] = "--complex";
	flags_source[3] = "--adaptive";
	if (ft_strcmp(str, "--bench") == 0)
	{
		if (flags->benchmark != -1)
			return (-1);
		return (flags->benchmark = 1, 1);
	}
	i = 0;
	while (i < 4)
	{
		if (ft_strcmp(str, flags_source[i]) == 0)
		{
			if (flags->method != -1)
				return (-1);
			return (flags->method = i, 1);
		}
		i++;
	}
	return (0);
}
