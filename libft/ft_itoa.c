/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/27 12:04:52 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/27 14:18:44 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static int	count_digits(int n)
{
	int	digits;

	digits = 1;
	if (n < 0)
	{
		if (n == -2147483648)
		{
			digits = 11;
			return (digits);
		}
		digits++;
		n = -n;
	}
	while (n > 9)
	{
		n = n / 10;
		digits++;
	}
	return (digits);
}

static char	*fill_str(char *s, int n, int digits)
{
	while (digits > 0)
	{
		s[digits] = n % 10 + 48;
		digits--;
		if (n > 9)
			n = n / 10;
	}
	if (s[0] != '-')
		s[0] = n % 10 + 48;
	return (s);
}

char	*ft_itoa(int n)
{
	int		digits;
	char	*s;

	digits = count_digits(n);
	s = malloc(digits + 1);
	if (!s)
		return (NULL);
	s[digits] = '\0';
	digits--;
	if (n < 0)
	{
		if (n == -2147483648)
		{
			ft_strlcpy(s, "-2147483648", digits + 2);
			return (s);
		}
		s[0] = '-';
		n = -n;
	}
	s = fill_str(s, n, digits);
	return (s);
}
