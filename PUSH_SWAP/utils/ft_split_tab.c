/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split_tab.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 16:15:46 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/30 13:05:06 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	is_sep(char c, char sep1, char sep2)
{
	if (c == sep1 || c == sep2 || c == '\0')
		return (1);
	return (0);
}

static char	**make_matrix(char const *s, char c, char c2)
{
	size_t	i;
	size_t	words;
	char	**result;

	i = 0;
	words = 0;
	if (!s)
		return (NULL);
	while (s[i])
	{
		if ((i == 0 || is_sep(s[i - 1], c, c2)) && !is_sep(s[i], c, c2))
			words++;
		i++;
	}
	result = (char **)malloc(sizeof(char *) * (words + 1));
	if (!result)
		return (NULL);
	return (result);
}

static char	**ft_free(char **result, size_t j)
{
	while (j > 0)
	{
		free(result[j - 1]);
		j--;
	}
	free(result);
	return (NULL);
}

static char	*new_arr(char const *s, size_t start, size_t final)
{
	char	*w;
	size_t	len;

	len = final - start + 1;
	w = (char *)malloc(len + 1);
	if (!w)
		return (NULL);
	ft_strlcpy(w, s + start, len + 1);
	return (w);
}

char	**ft_split_tab(char const *s, char c, char c2)
{
	char	**result;
	size_t	i;
	size_t	start;
	size_t	j;

	result = make_matrix(s, c, c2);
	if (!result)
		return (NULL);
	i = 0;
	j = 0;
	while (s[i])
	{
		if ((i == 0 || is_sep(s[i - 1], c, c2)) && !is_sep(s[i], c, c2))
			start = i;
		if (!is_sep(s[i], c, c2) && (is_sep(s[i + 1], c, c2)))
		{
			result[j] = new_arr(s, start, i);
			if (!result[j])
				return (ft_free(result, j));
			j++;
		}
		i++;
	}
	result[j] = NULL;
	return (result);
}
