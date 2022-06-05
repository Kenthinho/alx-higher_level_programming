#include <Python.h>

void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		int size, i;
		PyListObject *listobj = (PyListObject *)p;
		PyObject *obj;

		size = PyList_Size(p);
		printf("[*] Size of the python list = %d\n", size);
		printf("[*] Allocated = %li\n", listobj->allocated);
		i = 0;
		while (i < size)
		{
			obj = Pylist_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
			i++;
		}
	}
}
