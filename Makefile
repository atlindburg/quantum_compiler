# Compiler and linker
CC = gcc

# Flags for compiler
CFLAGS = -Iinclude -I/home/vboxuser/quantum_compiler/Unity/src -Wall -g

# Object files directory
OBJ_DIR = obj

# Library directory
LIB_DIR = lib

# Source files directory (for non-test sources)
SRC_DIR = src

# Output binary for the main application
OUT = quantum_simulator

# Source and object files for the main application
SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Test suite output executable
TEST_OUT = all_tests.out

# Explicitly listing all test source files, including all_tests.c
# Assuming all_tests.c is in the tests directory and not listing individual test module source files here
TEST_SRC = tests/all_tests.c

# Corresponding object file for all_tests.c
TEST_OBJ = $(OBJ_DIR)/all_tests.o

# Object files for individual test modules and Unity (assuming unity.c is in the specified Unity src directory)
# Add object files for your test modules (excluding the main test runner all_tests.c)
TEST_MODULE_OBJS = $(OBJ_DIR)/test_qubit.o $(OBJ_DIR)/test_xgate.o $(OBJ_DIR)/unity.o

# Object files for the implementations being tested
IMPL_OBJS = $(OBJ_DIR)/qubit.o $(OBJ_DIR)/xgate.o

# Rule for compiling the source files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Rule for compiling test object files (including unity.c and test modules)
$(OBJ_DIR)/%.o: tests/%.c
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR)/%.o: /home/vboxuser/quantum_compiler/Unity/src/%.c
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Rule for running tests (linking the test suite executable)
test: $(TEST_OUT)

$(TEST_OUT): $(TEST_OBJ) $(TEST_MODULE_OBJS) $(IMPL_OBJS)
	$(CC) $(CFLAGS) -o $@ $^ -L$(LIB_DIR) -lgsl -lgslcblas -lm

# Default rule to build the whole project
all: $(OUT)

# Rule for linking the main application program
$(OUT): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ -L$(LIB_DIR) -lgsl -lgslcblas -lm

# Rule to clean the workspace
clean:
	rm -f $(OUT) $(OBJS) $(TEST_OUT) $(TEST_OBJ) $(TEST_MODULE_OBJS) $(IMPL_OBJS)
	rm -rf $(OBJ_DIR)

.PHONY: all test clean

