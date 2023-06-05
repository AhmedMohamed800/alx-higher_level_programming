#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: list to be checked
* Return: 1 there is a cycles - 0 is the opposite
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listnode_t *head = NULL;

	while (list != NULL)
	{
		current = list;
		list = list->next;
		add_node_cycle(&head, current);
		if (check_containg_node(head, list))
		{
			free_listnode(head);
			return (1);
		}
	}
	free_listnode(head);
	return (0);
}

/**
* add_node_cycle - add a node to a list
* @head: the head of the list
* @node: node to be added
* Return: a node
*/
listnode_t *add_node_cycle(listnode_t **head, listint_t *node)
{
	listnode_t *new;

	new = malloc(sizeof(listnode_t));
	if (new == NULL)
		return (NULL);
	new->node = node;
	new->next = *head;
	*head = new;

	return (new);
}

/**
* check_containg_node - check if the node is equal to another node
* @head: node's head
* @node: node to be compared
* Return: 0 and 1
*/
int check_containg_node(listnode_t *head, listint_t *node)
{
	listnode_t *current;

	current = head;
	while (head != NULL)
	{
		current = head;
		head = head->next;
		if (current->node == node)
			return (1);
	}
	return (0);
}

/**
* free_listnode - free a list
* @head: list's head
* Return: nothing
*/
void free_listnode(listnode_t *head)
{
	listnode_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
