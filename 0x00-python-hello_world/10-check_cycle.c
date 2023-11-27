#include "lists.h"

/**
 * check_cycle - Checks for a loop in a linked list.
 * @list: Head of the linked list.
 *
 * Description: This function checks if a linked list has a loop.
 *
 * Return: 1 if there is a loop, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	/* Check if the list is empty */
	if (!list)
	{
		return (0);
	}

	slow = list;
	fast = list->next;

	/* Iterate through the list with slow and fast pointers */
	while (fast && slow && fast->next)
	{
		/* If there is a loop, slow and fast pointers will meet */
		if (slow == fast)
		{
			return (1); /* There is a loop */
		}

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0); /* No loop found */
}
