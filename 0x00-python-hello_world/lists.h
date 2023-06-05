#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct listnode_s - singly linked list
 * @node: node
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listnode_s
{
	listint_t *node;
	struct listnode_s *next;
} listnode_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
listnode_t *add_node_cycle(listnode_t **head, listint_t *node);
int check_containg_node(listnode_t *head, listint_t *node);
void free_listnode(listnode_t *head);

#endif /* LISTS_H */
