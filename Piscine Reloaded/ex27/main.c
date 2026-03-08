/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/14 09:39:06 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/14 12:40:20 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>

int	main(int argc, char **argv)
{
	int		fd;
	ssize_t	bytes;
	char	buffer[1000];

	if (argc == 1)
		return (write(2, "File name missing.\n", 19));
	if (argc > 2)
		return (write(2, "Too many arguments.\n", 20));
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (write(2, "Cannot read file.\n", 18));
	bytes = 1;
	while (bytes > 0)
	{
		bytes = read(fd, buffer, sizeof(buffer));
		write(1, buffer, bytes);
	}
	if (bytes == -1)
		return (write(2, "Cannot read file.\n", 18));
	close(fd);
	return (0);
}
