/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 12:50:29 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/10 12:51:55 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}
/*
int main(void)
{
    int x;
    int y;

    x = 1;
    y = 2;
    ft_div_mod(11, 2, &x, &y);
    printf("%d\n", x);
    printf("%d\n", y);
}*/
