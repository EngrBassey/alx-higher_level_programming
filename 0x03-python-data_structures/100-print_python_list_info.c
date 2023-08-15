#include <Python.h>

/**
  * print_python_list_info - function that print some basic infp about python
  * @p: Objects
  */

void print_python_list_info(PyObject *p)
{
	int size, ptr, i;
	PyObject *obj;

	size = Py_size(p);
	ptr = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ptr);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
