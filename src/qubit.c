// qubit.c

#include "quantum_sim.h"

// Initialize a qubit with given amplitudes for |0> and |1> states
void initialize_qubit(Qubit *q, double complex state0, double complex state1) {
    q->state0 = state0;
    q->state1 = state1;
}

