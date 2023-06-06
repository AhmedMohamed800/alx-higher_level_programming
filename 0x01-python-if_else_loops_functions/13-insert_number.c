#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* insert_node - insert a node
* @head: the nodes heads
* @number: number to be inserted
* Return: node
*/
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
		if (current->next == NULL)
		{
			current->next = new;
			new->next = NULL;
			break;
		}
		else if (number <= current->next->n)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		current = current->next;
	}
	return (new);
}

