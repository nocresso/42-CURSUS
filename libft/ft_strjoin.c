/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:15:41 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/23 12:52:49 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	len1;
	char	*c;
	size_t	i;

	len1 = ft_strlen(s1);
	c = (char *)malloc(len1 + ft_strlen(s2) + 1);
	if (!c)
		return (NULL);
	i = 0;
	while (s1[i])
	{
		c[i] = s1[i];
		i++;
	}
	i = 0;
	while (s2[i])
	{
		c[len1] = s2[i];
		i++;
		len1++;
	}
	c[len1] = '\0';
	return (c);
}
