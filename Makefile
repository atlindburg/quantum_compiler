# Compiler and linker
CC = gcc

# Flags for compiler
CFLAGS = -Iinclude -Wall -g

# Source files directory
SRC_DIR = src

# Object files directory
OBJ_DIR = obj

# Library directory
LIB_DIR = lib

# Source files
SRCS = $(wildcard $(SRC_DIR)/*.c)

# Object files
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Output binary
OUT = quantum_simulator

# Default rule to build the whole project
all: $(OUT)

# Rule for linking the program
$(OUT): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ -L$(LIB_DIR) -lgsl -lgslcblas -lm

# Rule for compiling the source files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Test variables
TEST_SRC = $(wildcard tests/*.c)
TEST_OBJ = $(patsubst tests/%.c,$(OBJ_DIR)/%.o,$(TEST_SRC))
TEST_OUT = test_qubit

# Rule for running tests
test: $(TEST_OUT)

$(TEST_OUT): $(TEST_OBJ) $(OBJ_DIR)/qubit.o
	$(CC) $(CFLAGS) -o $@ $^ -L$(LIB_DIR) -lgsl -lgslcblas -lm

# Pattern rule for compiling test objects
$(OBJ_DIR)/%.o: tests/%.c
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Rule to clean the workspace
clean:
	rm -f $(OUT) $(OBJS)
	rm -rf $(OBJ_DIR)
	rm -f $(TEST_OUT) $(TEST_OBJ)

.PHONY: all test clean
