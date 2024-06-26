#include "../include/quantum_sim.h"
#include "../include/all_tests.h"

// Inside all_tests.c
int main(void) {
    UNITY_BEGIN();

    // Call the test runner functions for each test module
    test_qubit_run_tests();
    test_xgate_run_tests();
    test_measurement_run_tests(); // Call the measurement test suite runner

    return UNITY_END();
}
