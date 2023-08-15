#include "lists.h"

/**
  * is_palindrome - function that checks a palindrom
  * @head: the pointer to the first node
  * Return: 1 on success
  */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = reverse(&slow);
	fast = *head;

	while (fast != NULL && slow != NULL)
	{
		if (fast->n != slow->n)
		{
			return (0);
		}
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}

/**
  * reverse - function that reverse a list
  * @head: pointer to the first node
  * Return: head
  */

listint_t *reverse(listint_t **head)
{

	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;

		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
