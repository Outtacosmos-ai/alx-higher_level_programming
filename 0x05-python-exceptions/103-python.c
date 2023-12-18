#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints information about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p) 
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints information about Python bytes
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("size: %ld\n", size);
	printf("trying string: %s\n", PyBytes_AsString(p));

	printf("first 10 bytes:");
	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf(" %02hhx", ((char *)PyBytes_AsString(p))[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints information about Python float objects
 * @p: PyObject pointer
 */
void print_python_float(PyObject *p) 
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");
	printf("value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
