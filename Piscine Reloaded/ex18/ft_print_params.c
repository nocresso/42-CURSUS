/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_params.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 15:41:08 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/10 16:27:27 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);

int	main(int argc, char *argv[])
{
	int	a;
	int	j;

	a = 1;
	j = 0;
	while (a < argc)
	{
		j = 0;
		while (argv[a][j])
		{
			ft_putchar(argv[a][j]);
			j++;
		}
		ft_putchar('\n');
		a++;
	}
	return (0);
}
