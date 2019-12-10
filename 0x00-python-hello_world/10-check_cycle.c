#include "lists.h"

/**
* check_cycle - function in C that checks if a singly linked list has a cycle in it
* @list: the list to check
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *one, *two = NULL;

	one = two;
	two = list;

	while (one && two && two->next)
	{
		one = one->next;
		two = two->next->next;

		if (one == two)
		{
			one = list;
			while (one != NULL && two != NULL)
			{
				if (one == two)
					return (1);
				one = one->next;
				two = two->next;
			}
		}
	}
	return (0);
}
