#include "lists.h"

/**
  * check_cycle - check for cycle
  * @list: the list
  * Return: return 0
  */

int check_cycle(listint_t *list)
{
	listint_t *ptr_1 = list;
	listint_t *ptr_2 = list;

	while (ptr_1 != NULL && ptr_2 != NULL && ptr_2->next != NULL)
	{
		ptr_1 = ptr_1->next;
		ptr_2 = ptr_2->next->next;

		if (ptr_1 == ptr_2)
			return (1)
	}
	return (0);
}
