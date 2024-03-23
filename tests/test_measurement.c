#include "../include/quantum_sim.h"
#include "../include/all_tests.h"

// A simple assertion function to check measurement outcomes
void assertMeasurement(int expected, int actual, const char* testName) {
    if (expected == actual) {
        printf("PASS: %s\n", testName);
    } else {
        printf("FAIL: %s - Expected %d, got %d\n", testName, expected, actual);
    }
}

// Example test function
void testMeasure0State() {
    Qubit q;
    initialize_qubit(&q, 1, 0); // Initialize qubit to |0> state
    int measurement = measure(&q);
    assertMeasurement(0, measurement, "testMeasure0State");
}

void test_measurement_run_tests(void) {
    RUN_TEST(testMeasure0State);
    // Add RUN_TEST for any additional measurement tests you create
}
