/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/21 13:45:04 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/21 14:30:06 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	size_t	len;
	char	a;

	a = (char)c;
	len = ft_strlen(s);
	if (a == '\0')
		return ((char *)(s + len));
	while (len > 0)
	{
		if (s[len - 1] == a)
			return ((char *)(s + len - 1));
		len--;
	}
	return (NULL);
}
