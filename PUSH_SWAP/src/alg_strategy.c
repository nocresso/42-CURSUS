/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   alg_strategy.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 18:50:44 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/30 19:56:24 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	alg_selection(t_list **stack_a, t_flags *flags, t_bench *bench)
{
	int		size;
	t_list	*stack_b;
	float	disorder;

	size = ft_lstsize(*stack_a);
	stack_b = NULL;
	disorder = index_order(stack_a);
	if (bench)
		bench->disorder = disorder;
	stack_index(*stack_a, size);
	if (disorder == 0)
		return (0);
	if (flags->method == 0)
		simple_sort(stack_a, &stack_b, size, bench);
	else if (flags->method == 1)
		chunks_sort(stack_a, &stack_b, size, bench);
	else if (flags->method == 2)
		radix_sort(stack_a, &stack_b, size, bench);
	else
		if (!adaptative_sort(stack_a, &stack_b, size, bench))
			return (0);
	free_node(&stack_b);
	print_bench(flags, bench);
	return (1);
}

static void	assign_strategy(t_bench *bench, float disorder, int size)
{
	if (bench)
	{
		if (size <= 5)
			bench->strategy = "Adaptive / O(n²)";
		else if (disorder < 0.2)
			bench->strategy = "Adaptive / O(n²)";
		else if (disorder >= 0.2 && disorder < 0.5)
			bench->strategy = "Adaptive / O(n√n)";
		else if (disorder >= 0.5)
			bench->strategy = "Adaptive / O(n log n)";
	}
}

int	adaptative_sort(t_list **stack_a, t_list **stack_b, int size,
	t_bench *bench)
{
	float	disorder;

	stack_index(*stack_a, size);
	disorder = index_order(stack_a);
	assign_strategy(bench, disorder, size);
	if (size <= 5)
		sort_small(stack_a, stack_b, size, bench);
	else if (disorder < 0.2)
		simple_sort(stack_a, stack_b, size, bench);
	else if (disorder >= 0.2 && disorder < 0.5)
		chunks_sort(stack_a, stack_b, size, bench);
	else if (disorder >= 0.5)
		radix_sort(stack_a, stack_b, size, bench);
	return (1);
}
