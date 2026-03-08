/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 15:42:06 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/23 11:28:04 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*Reserva espacio de almacenamiento para una copia de una string. Devuelve un 
 puntero al espacio de almacenamiento de la string copiada.*/

#include <stdlib.h>
#include "libft.h"

char	*ft_strdup(const char *str)
{
	char	*c;
	size_t	len;
	size_t	i;

	len = ft_strlen(str);
	i = 0;
	c = (char *)malloc(sizeof(char) * (len + 1));
	if (!c)
		return (NULL);
	while (str[i])
	{
		c[i] = str[i];
		i++;
	}
	c[i] = '\0';
	return (c);
}
