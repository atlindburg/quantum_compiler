// qubit.h

#ifndef QUBIT_H
#define QUBIT_H

typedef struct {
    double state0_real;
    double state0_imag;
    double state1_real;
    double state1_imag;
} Qubit;

// Function declarations related to qubit operations
void initialize_qubit(Qubit *q, double state0_real, double state0_imag, double state1_real, double state1_imag);

#endif // QUBIT_H

