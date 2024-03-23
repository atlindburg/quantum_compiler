#include "../include/quantum_sim.h"

void compile(const char* sourceCode) {
    printf("Compiling the source code...\n");

    // Initialize Python
    Py_Initialize();

    // Run the Python lexer
    PyObject* pName = PyUnicode_DecodeFSDefault("lexer"); // Assuming your Python lexer is in 'lexer_module.py'
    PyObject* pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL) {
        PyObject* pFunc = PyObject_GetAttrString(pModule, "lexer");
        if (pFunc && PyCallable_Check(pFunc)) {
            PyObject* pArgs = PyTuple_New(1);
            PyObject* pValue = PyUnicode_FromString(sourceCode);
            PyTuple_SetItem(pArgs, 0, pValue);

            PyObject* pResult = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);
            if (pResult != NULL) {
                // Handle tokens returned by lexer
                printf("Lexer returned something.\n");
                Py_DECREF(pResult);
            } else {
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                PyErr_Print();
                fprintf(stderr, "Call to lexer failed.\n");
                return;
            }
        } else {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"lexer\".\n");
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    } else {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"lexer_module\".\n");
        return;
    }

    // Finalize Python
    Py_Finalize();
}

