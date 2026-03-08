/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_numbers.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 15:43:39 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/07 17:26:22 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_number(int n)
{
	char	r;
	int		i;

	i = 0;
	if (n < 0)
	{
		write(1, "-", 1);
		i++;
		if (n == -2147483648)
		{
			write(1, "2147483648", 10);
			return (i + 10);
		}
		n = -n;
	}
	if (n > 9)
	{
		i = i + print_number(n / 10);
	}
	r = n % 10 + 48;
	write(1, &r, 1);
	i++;
	return (i);
}

int	print_unsign_int(unsigned int n)
{
	char	r;
	int		i;

	i = 0;
	if (n > 9)
	{
		i = i + print_unsign_int(n / 10);
	}
	r = n % 10 + 48;
	write(1, &r, 1);
	i++;
	return (i);
}

int	print_low_hex(unsigned int n)
{
	int		r;
	int		i;
	char	*hex;

	i = 0;
	hex = "0123456789abcdef";
	if (n > 15)
		i = i + print_low_hex(n / 16);
	r = n % 16;
	write(1, &hex[r], 1);
	i++;
	return (i);
}

int	print_up_hex(unsigned int n)
{
	int		r;
	int		i;
	char	*hex;

	i = 0;
	hex = "0123456789ABCDEF";
	if (n > 15)
		i = i + print_up_hex(n / 16);
	r = n % 16;
	write(1, &hex[r], 1);
	i++;
	return (i);
}
