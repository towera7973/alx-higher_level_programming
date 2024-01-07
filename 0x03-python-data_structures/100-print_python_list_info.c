#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - shows size,allocated space and type of elements of  Python lists pointed by c object(p) in c language
 * @p: object
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, space_allocated, i;

	i = 0;
	PyObject *container;

	list_size = PyList_Size(p);
	space_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", space_allocated);
	while (i < list_size)
	{
		container = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(container)->tp_name);
		i++;
	}
}
