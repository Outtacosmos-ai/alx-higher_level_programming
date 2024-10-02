#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

void print_python_string(PyObject *p)
{
    const char *type = NULL;
    Py_ssize_t length;
    wchar_t *str;

    printf("[.] string object info\n");
    
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        type = "compact ascii";
    else
        type = "compact unicode object";

    length = PyUnicode_GET_LENGTH(p);
    str = PyUnicode_AsWideCharString(p, &length);

    printf("  type: %s\n", type);
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", str);

    PyMem_Free(str);
}
