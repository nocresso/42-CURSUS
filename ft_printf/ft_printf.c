/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 15:36:32 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/07 17:25:45 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	find_format(char c, va_list *args)
{
	if (c == 'c')
		return ((print_char(va_arg(*args, int))));
	else if (c == 's')
		return (print_string(va_arg(*args, char *)));
	else if (c == 'p')
		return (print_pointer(va_arg(*args, void *)));
	else if (c == 'i' || c == 'd')
		return (print_number(va_arg(*args, int)));
	else if (c == 'u')
		return (print_unsign_int(va_arg(*args, unsigned int)));
	else if (c == 'x')
		return (print_low_hex(va_arg(*args, unsigned int)));
	else if (c == 'X')
		return (print_up_hex(va_arg(*args, unsigned int)));
	else if (c == '%')
		return (print_char('%'));
	else
		return (0);
}

int	ft_printf(char const *str, ...)
{
	va_list	args;
	int		i;
	int		total;

	i = 0;
	total = 0;
	va_start(args, str);
	while (str[i])
	{
		if (str[i] != '%')
		{
			total = total + print_char(str[i]);
			i++;
		}
		else if (str[i] == '%' && str[i + 1])
		{
			total = total + find_format(str[i + 1], &args);
			i = i + 2;
		}
		else
			i++;
	}
	va_end(args);
	return (total);
}
