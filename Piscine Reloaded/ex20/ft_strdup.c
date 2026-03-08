/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 16:19:19 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/13 10:38:55 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		i++;
	}
	return (i);
}

char	*ft_strdup(char *src)
{
	char	*c;
	char	*start;

	c = (char *)malloc((ft_strlen(src) + 1) * sizeof(char));
	if (c == NULL)
		return (NULL);
	start = c;
	while (*src)
	{
		*c = *src;
		c++;
		src++;
	}
	*c = '\0';
	return (start);
}
/*
int	main(void)
{
	char	*x = ft_strdup("Hello world");
	printf("%s\n", x);
}*/
