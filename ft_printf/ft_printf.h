/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 17:30:45 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/07 17:30:50 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int	print_number(int n);
int	print_unsign_int(unsigned int n);
int	print_low_hex(unsigned int n);
int	print_up_hex(unsigned int n);
int	print_pointer(void *c);
int	print_char(char c);
int	print_string(char *str);
int	find_format(char c, va_list *args);
int	ft_printf(char const *str, ...);

#endif
