// qubit.c

#include "quantum_sim.h"

// Updated function to match the new struct definition
void initialize_qubit(Qubit *q, double state0_real, double state0_imag, double state1_real, double state1_imag) {
    printf("Initializing qubit with:\n");
    printf("state0_real: %f, state0_imag: %f\n", state0_real, state0_imag);
    printf("state1_real: %f, state1_imag: %f\n", state1_real, state1_imag);
    q->state0_real = state0_real;
    q->state0_imag = state0_imag;
    q->state1_real = state1_real;
    q->state1_imag = state1_imag;
}
