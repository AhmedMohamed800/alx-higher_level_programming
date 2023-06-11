#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: linked list head
 * Return: 1 on success, 0 on failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *second = *head;
	int size_of_list = 1;
	int *numys, i = 0, j = 0, t = 0;

	if (current == NULL || current->next == NULL)
		return (1);
	while (current->next != NULL)
	{
		current = current->next;
		size_of_list++;
	}
	if (size_of_list % 2 == 0)
	{
		numys = malloc(size_of_list * sizeof(int));
		while (second != NULL)
		{
			numys[t] = second->n;
			second = second->next;
			t++;
		}
		j = size_of_list - 1;
		for (i = 0; i < size_of_list / 2; i++)
		{
			if (numys[i] != numys[j])
				return (0);
			j--;
		}
		free(numys);
		return (1);
	}
	return (0);
}
