// qubit.h

#ifndef QUBIT_H
#define QUBIT_H

typedef struct {
    double complex state0;  // Amplitude for |0>
    double complex state1;  // Amplitude for |1>
} Qubit;

// Function declarations related to qubit operations
void initialize_qubit(Qubit *q, double complex state0, double complex state1);
void apply_x_gate(Qubit *q);

#endif // QUBIT_H

