# Quantum Computing Simulation Project

This project aims to develop a quantum computing simulation, focusing on implementing quantum gates and operations in C. The simulation allows for experimenting with quantum algorithms without the need for actual quantum hardware.

## Project Structure

The project is structured as follows:

- `src/`: Contains all source code for the simulation.
  - `main.c`: The entry point of the simulation.
  - `xgate.c`: Implementation of the X (Pauli-X) gate.
  - `xgate.h`: Header file for the X gate implementation.
- `tests/`: Contains Unity-based tests for the quantum operations.
  - `test_xgate.c`: Tests for the X gate functionality.
- `Unity/`: Unity testing framework cloned from [ThrowTheSwitch/Unity](https://github.com/ThrowTheSwitch/Unity).
- `Makefile`: Automates the compilation of the project and tests.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Getting Started

### Prerequisites

- GCC compiler
- Git

### Setting Up the Project

1. **Clone the Repository**

   ```sh
   git clone <repository-URL>
   cd quantum_compiler

