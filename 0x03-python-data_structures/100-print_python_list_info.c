#include <Python.h>
#include "object.h"
#include "listobject.h"

/**
  * print_python_list_info - function that print some basic infp about python
  * @p: Objects
  */

void print_python_list_info(PyObject *p)
{
	int size, alloc_mem, i;
	PyObject *obj;
	size = Py_SIZE(p);
	alloc_mem = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc_mem);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
