/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 19:06:44 by nocrespo          #+#    #+#             */
/*   Updated: 2026/01/17 10:06:18 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

char	*read_fd(int fd, char *save, char *buffer)
{
	ssize_t	bytes;
	char	*tmp;

	bytes = read(fd, buffer, BUFFER_SIZE);
	while (bytes > 0)
	{
		buffer[bytes] = '\0';
		if (save == NULL)
			tmp = ft_strdup(buffer);
		else
			tmp = ft_strjoin(save, buffer);
		if (!tmp)
			return (free(save), NULL);
		free(save);
		save = tmp;
		if (ft_strchr(save, '\n') != NULL)
			return (save);
		bytes = read(fd, buffer, BUFFER_SIZE);
	}
	if (bytes == -1)
		return (free(save), NULL);
	return (save);
}

char	*create_line(char **save)
{
	ssize_t	i;
	char	*line;
	char	*rest;

	line = NULL;
	i = 0;
	while ((*save)[i] != '\n')
		i++;
	line = ft_substr(*save, 0, i + 1);
	if (line == NULL)
		return (free(line), NULL);
	rest = ft_substr(*save, i + 1, (ft_strlen(*save) - i - 1));
	free(*save);
	if (rest == NULL)
		return (*save = NULL, NULL);
	if (rest[0] == '\0')
	{
		free(rest);
		*save = NULL;
	}
	else
		*save = rest;
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*save[1024];
	char		*line;
	char		*buffer;

	if (fd < 0 || fd >= 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buffer)
		return (NULL);
	line = NULL;
	save[fd] = read_fd(fd, save[fd], buffer);
	free(buffer);
	if (save[fd] == NULL)
		return (NULL);
	if (ft_strchr(save[fd], '\n') != NULL)
		return (create_line(&save[fd]));
	line = ft_strdup(save[fd]);
	free(save[fd]);
	save[fd] = NULL;
	return (line);
}
