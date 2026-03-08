/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 12:52:42 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/10 12:55:05 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	f;

	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	f = nb;
	while (nb > 1)
	{
		f = f * (nb - 1);
		nb--;
	}
	return (f);
}
/*
int main(void)
{
    int nb;
    
    nb = 5;
    printf("%d\n", ft_iterative_factorial(nb));
}*/
