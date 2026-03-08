/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_pointer.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 16:19:52 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/07 17:56:17 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	print_hex_long(unsigned long n)
{
	int		r;
	int		i;
	char	*hex;

	i = 0;
	hex = "0123456789abcdef";
	if (n > 15)
		i = i + print_hex_long(n / 16);
	r = n % 16;
	write(1, &hex[r], 1);
	i++;
	return (i);
}

int	print_pointer(void *c)
{
	char			*hex;
	int				i;
	unsigned long	u;

	if (c == NULL)
		return (write(1, "(nil)", 5));
	u = (unsigned long)c;
	hex = "0123456789abcdef";
	write(1, "0x", 2);
	i = 2;
	i = i + print_hex_long(u);
	return (i);
}
