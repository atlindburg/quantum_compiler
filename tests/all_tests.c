#include "../include/quantum_sim.h"
#include "../include/qubit.h"
#include "../include/xgate.h"
#include "../include/test_qubit.h"
#include "../include/test_xgate.h"
#include "../Unity/src/unity.h"

// Inside all_tests.c
int main(void) {
    UNITY_BEGIN();

    // Call the test runner functions for each test module
    test_qubit_run_tests();
    test_xgate_run_tests();

    return UNITY_END();
}
