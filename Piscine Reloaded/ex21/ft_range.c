/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 11:01:41 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/13 11:18:57 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
//#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	dif;
	int	*c;
	int	*start;

	dif = max - min;
	c = (int *)malloc(dif * sizeof(int));
	start = c;
	if (c == NULL || dif <= 0)
		return (NULL);
	while (min < max)
	{
		*c = min;
		c++;
		min++;
	}
	return (start);
}
/*
int main(void)
{
    int min = 2;
    int max = 8;
    int x = max - min;
    int i = 0;
    int *a = ft_range(min, max);
    while (i < x)
    {
        printf("%d\n", a[i]);
        i++;
    }
    free(a);
    return (0);
}
*/
