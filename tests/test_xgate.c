#include "unity.h"
#include "xgate.h"

void setUp(void) {
    // set stuff up here
}

void tearDown(void) {
    // clean stuff up here
}

void test_xgate_flips_qubit(void) {
    int qubit = 0;
    XGate(&qubit);
    TEST_ASSERT_EQUAL_INT(1, qubit);

    qubit = 1;
    XGate(&qubit);
    TEST_ASSERT_EQUAL_INT(0, qubit);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_xgate_flips_qubit);
    return UNITY_END();
}

