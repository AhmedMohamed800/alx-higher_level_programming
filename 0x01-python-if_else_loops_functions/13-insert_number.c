#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || number < current->n)
	{
		*head = new;
		new->next = current;
		return (new);
	}
	while (current != NULL)
	{
		if (number == current->n ||
				(number > current->n && number < current->next->n))
		{
			current->next = new;
			new->next = current->next;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	new->next = NULL;
	return (new);
}
