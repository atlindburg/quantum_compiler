#include "../include/quantum_sim.h"
#include "../include/all_tests.h"

void test_qubit_initialization(void) {
    Qubit q;
    double complex initial_state0 = 1 + 0 * I; // |0> state
    double complex initial_state1 = 0 + 0 * I; // |1> state

    initialize_qubit(&q, initial_state0, initial_state1);

    TEST_MESSAGE("Testing qubit initialization to |0> state.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(1, creal(q.state0), "Real part of state0 should be 1.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(0, cimag(q.state0), "Imaginary part of state0 should be 0.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(0, creal(q.state1), "Real part of state1 should be 0.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(0, cimag(q.state1), "Imaginary part of state1 should be 0.");
}

void test_apply_x_gate(void) {
    Qubit q;
    double complex initial_state0 = 1 + 0 * I; // Initially in |0>
    double complex initial_state1 = 0 + 0 * I; // Initially not in |1>

    initialize_qubit(&q, initial_state0, initial_state1);
    apply_x_gate(&q); // Apply X gate, should swap states

    TEST_MESSAGE("Testing X gate application, expecting qubit state to flip.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(0, creal(q.state0), "After X gate, real part of state0 should be 0.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(0, cimag(q.state0), "After X gate, imaginary part of state0 should be 0.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(1, creal(q.state1), "After X gate, real part of state1 should be 1.");
    TEST_ASSERT_EQUAL_DOUBLE_MESSAGE(0, cimag(q.state1), "After X gate, imaginary part of state1 should be 0.");
}

int test_qubit_run_tests(void) {
    UNITY_BEGIN();
    RUN_TEST(test_qubit_initialization);
    RUN_TEST(test_apply_x_gate);
    return UNITY_END();
}

