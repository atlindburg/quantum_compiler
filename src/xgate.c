// xgate.c
#include "quantum_sim.h"

// Implementation of the XGate function
void XGate(int *qubit) {
    // Assuming a simple model where a qubit is represented as a binary state:
    // Flip the qubit value: if 0 then 1, if 1 then 0.
    *qubit = !(*qubit);
}

