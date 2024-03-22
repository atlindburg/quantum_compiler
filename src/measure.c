#include "../include/quantum_sim.h"
#include "../include/all_tests.h"

int measure(Qubit *q) {
    // Seed the random number generator only once
    // (Call this somewhere in the initialization part of your program)
    // srand(time(NULL));

    // Calculate the probabilities of the qubit collapsing to |0> or |1>
    double prob0 = creal(q->state0) * creal(q->state0) + cimag(q->state0) * cimag(q->state0);
    double prob1 = creal(q->state1) * creal(q->state1) + cimag(q->state1) * cimag(q->state1);

    // Generate a random number between 0 and 1
    double random = (double)rand() / RAND_MAX;

    // Collapse based on the calculated probabilities
    if (random < prob0 / (prob0 + prob1)) { // Normalize probabilities
        // Collapse to |0>
        return 0;
    } else {
        // Collapse to |1>
        return 1;
    }
}

