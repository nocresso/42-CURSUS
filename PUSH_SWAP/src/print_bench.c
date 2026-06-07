/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bench.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/01 12:27:16 by nocrespo          #+#    #+#             */
/*   Updated: 2026/02/01 14:38:31 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	print_disorder(float n)
{
	float	disorder;
	int		num;
	int		dec;

	disorder = n * 10000;
	num = (int)disorder / 100;
	dec = (int)disorder % 100;
	ft_putnbr_fd(num, 2);
	write(2, ".", 1);
	if (dec < 10)
		write(2, "0", 1);
	ft_putnbr_fd(dec, 2);
	write(2, "%", 1);
}

static void	print_ops_num(char *str, int n)
{
	write(2, "[bench] ", 8);
	ft_putstr_fd(str, 2);
	write(2, " ops: ", 6);
	ft_putnbr_fd(n, 2);
	write(2, "\n", 1);
}

static void	print_bench_ops(t_bench *bench)
{
	print_ops_num("sa", bench->ops.sa);
	print_ops_num("sb", bench->ops.sb);
	print_ops_num("ss", bench->ops.ss);
	print_ops_num("pa", bench->ops.pa);
	print_ops_num("pb", bench->ops.pb);
	print_ops_num("ra", bench->ops.ra);
	print_ops_num("rb", bench->ops.rb);
	print_ops_num("rr", bench->ops.rr);
	print_ops_num("rra", bench->ops.rra);
	print_ops_num("rrb", bench->ops.rrb);
	print_ops_num("rrr", bench->ops.rrr);
}

void	print_bench(t_flags *flags, t_bench *bench)
{
	int	strat_len;

	if (flags->benchmark == 1)
	{
		write(2, "[bench] disorder: ", 19);
		print_disorder(bench->disorder);
		write(2, "\n", 1);
		if (bench->strategy == NULL)
		{
			if (flags->method == 0)
				bench->strategy = "Simple / O(n²)";
			else if (flags->method == 1)
				bench->strategy = "Medium / O(n√n)";
			else if (flags->method == 2)
				bench->strategy = "Complex / O(n log n)";
		}
		write(2, "[bench] strategy: ", 19);
		strat_len = ft_strlen(bench->strategy);
		write(2, bench->strategy, strat_len);
		write(2, "\n", 1);
		write(2, "[bench] total ops: ", 20);
		ft_putnbr_fd(bench->total_ops, 2);
		write(2, "\n", 1);
		print_bench_ops(bench);
	}
}
