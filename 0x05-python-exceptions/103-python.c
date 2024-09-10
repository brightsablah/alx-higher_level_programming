#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * pirnt_python_list - print info about python lists
 * @p: object
 * Return: 0 or error
 */
void print_python_list(PyObject *p)
{


}

/**
 * pirnt_python_bytes - print info about python bytes
 * @p: object
 * Return: 0 or error
 */
void print_python_bytes(PyObject *p)
{


}

/**
 * pirnt_python_float - print info about python float objects
 * @p: object
 * Return: 0 or error
 */
void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");

    if (!Pyfloat_Check(p))
    {
        printf(" [ERROR] Invalid Float Object\n");
        return;
    }

    /* accessing float value and printing result */
    double float_value = ((PyFloatObject *)p)->ob_fval;
    printf(" value: %g\n", float_value);
}