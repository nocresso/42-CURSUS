/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelona.co  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 13:27:49 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/30 11:08:45 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	lensrc;
	size_t	lendst;
	size_t	i;
	size_t	j;

	lensrc = ft_strlen(src);
	if (size <= ft_strlen(dst))
		return (size + lensrc);
	i = 0;
	lendst = ft_strlen(dst);
	j = lendst;
	while (src[i] && j < (size - 1))
	{
		dst[j++] = src[i++];
	}
	if (j < size)
		dst[j] = '\0';
	return (lendst + lensrc);
}
