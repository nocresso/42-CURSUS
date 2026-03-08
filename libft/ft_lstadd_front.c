/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nocrespo <nocrespo@student.42barcelon      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/28 10:54:25 by nocrespo          #+#    #+#             */
/*   Updated: 2025/12/28 11:28:04 by nocrespo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*primero se usa el puntero new para apuntar al que era el primer nodo de la
 lista, despues se cambia el puntero *lst para que apunte al que es ahora el
 primer nodo.*/

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	new->next = *lst;
	*lst = new;
}
