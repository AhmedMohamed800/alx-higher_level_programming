#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		if (number > current->n && number < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		else if (current->next = NULL)
		{
			new->next = NULL;
			current->next = new;
			break;
		}
		current = current->next;
	}
	return (new);
}
