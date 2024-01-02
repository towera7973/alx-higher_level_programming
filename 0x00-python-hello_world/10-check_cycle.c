/*
 * File: 10-check_cycle.c
 * Auth: Towera Mndoli
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *towera, *mndoli;

	if (list == NULL || list->next == NULL)
		return (0);

	towera = list->next;
	mndoli = list->next->next;

	while (towera  && mndoli && mndoli->next)
	{
		if (towera == mndoli)
			return (1);

		towera = towera->next;
		mndoli = mndoli->next->next;
	}

	return (0);
}
