/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 16:15:46 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/30 13:05:06 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static char	**make_matrix(char const *s, char c)
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
		if ((i == 0 || s[i - 1] == c) && s[i] != c)
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

char	**ft_split(char const *s, char c)
{
	char	**result;
	size_t	i;
	size_t	start;
	size_t	j;

	result = make_matrix(s, c);
	if (!result)
		return (NULL);
	i = 0;
	j = 0;
	while (s[i])
	{
		if ((i == 0 || s[i - 1] == c) && s[i] != c)
			start = i;
		if (s[i] != c && (s[i + 1] == c || s[i + 1] == '\0'))
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
