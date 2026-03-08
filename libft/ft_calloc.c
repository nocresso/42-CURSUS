/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 15:07:48 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/04 10:54:54 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	unsigned char	*c;
	size_t			total;

	if (!count || !size)
	{
		c = malloc(1);
		if (!c)
			return (NULL);
		return ((void *)c);
	}
	total = count * size;
	if ((total / size) != count)
		return (NULL);
	c = (unsigned char *)malloc(total);
	if (!c)
		return (NULL);
	ft_bzero((void *)c, total);
	return ((void *)c);
}
