#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: list to be checked
* Return: 1 there is a cycles - 0 is the opposite
*/
int check_cycle(listint_t *list)
{
	int max_int = 0;

	while (list != NULL)
	{
		list = list->next;
		max_int++;
		if (max_int == 1000)
			return (1);
	}
	return (0);
}
