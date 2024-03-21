# Compiler
CC = gcc

# Compiler Flags
CFLAGS = -Isrc -IUnity/src

# Source Files
SRC_FILES = $(wildcard src/*.c)

# Test Source Files (excluding the main application entry point)
TEST_SRC_FILES = $(wildcard tests/*.c) $(filter-out src/main.c, $(SRC_FILES))

# Unity Framework Files
UNITY_FILES = Unity/src/unity.c

# Output Binary for Main Program
MAIN_BIN = quantum_simulator

# Output Binary for Tests
TEST_BIN = run_tests

# Default Target
all: $(MAIN_BIN)

# Main Program Compilation
$(MAIN_BIN): $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

# Test Compilation and Execution
test: $(TEST_SRC_FILES) $(UNITY_FILES)
	$(CC) $(CFLAGS) $^ -o $(TEST_BIN)
	./$(TEST_BIN)

# Clean Target
clean:
	rm -f $(MAIN_BIN) $(TEST_BIN)

.PHONY: all test clean

