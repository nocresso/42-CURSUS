/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 12:57:38 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/10 12:59:07 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_sqrt(int nb)
{
	int	i;

	i = 1;
	while (i * i < nb)
	{
		i++;
	}
	if (i * i > nb)
		return (0);
	return (i);
}
/*
int main(void)
{
    int nb;
    
    nb = 25587155;
    printf("%d\n", ft_sqrt(nb));
}*/
