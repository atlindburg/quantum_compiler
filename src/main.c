#include "quantum_sim.h"

int main() {
    int qubit = 0; // Assume 0 represents the |0⟩ state
    printf("Initial qubit state: %d\n", qubit);

    XGate(&qubit); // Apply the X gate
    printf("Qubit state after XGate: %d\n", qubit); // Expect 1, representing the |1⟩ state

    return 0;
}

