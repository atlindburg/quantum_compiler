#include "../include/quantum_sim.h"
#include "../include/qubit.h"
#include "../include/xgate.h"
#include "../include/test_qubit.h"
#include "../Unity/src/unity.h"

void test_qubit_initialization(void) {
    Qubit q;
    double complex initial_state0 = 1 + 0 * I; // |0> state
    double complex initial_state1 = 0 + 0 * I; // |1> state

    initialize_qubit(&q, initial_state0, initial_state1);
    TEST_ASSERT_EQUAL_DOUBLE(1, creal(q.state0));
    TEST_ASSERT_EQUAL_DOUBLE(0, cimag(q.state0));
    TEST_ASSERT_EQUAL_DOUBLE(0, creal(q.state1));
    TEST_ASSERT_EQUAL_DOUBLE(0, cimag(q.state1));
}

void test_apply_x_gate(void) {
    Qubit q;
    double complex initial_state0 = 1 + 0 * I; // Initially in |0>
    double complex initial_state1 = 0 + 0 * I; // Initially not in |1>

    initialize_qubit(&q, initial_state0, initial_state1);
    apply_x_gate(&q); // Apply X gate, should swap states

    // Now, qubit should be in |1> state
    TEST_ASSERT_EQUAL_DOUBLE(0, creal(q.state0));
    TEST_ASSERT_EQUAL_DOUBLE(0, cimag(q.state0));
    TEST_ASSERT_EQUAL_DOUBLE(1, creal(q.state1));
    TEST_ASSERT_EQUAL_DOUBLE(0, cimag(q.state1));
}

int test_qubit_run_tests(void) {
    UNITY_BEGIN();

    RUN_TEST(test_qubit_initialization);
    RUN_TEST(test_apply_x_gate);

    return UNITY_END();
}

