# Makefile for a C++ project

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -Wextra -std=c++17

# Target executable name
TARGET = my_program

# Source files
SOURCES = main.cpp

# Object files
OBJECTS = $(SOURCES:.cpp=.o)

# Build the target executable
build: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET)

# Compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Run tests (placeholder, customize as needed)
test:
	@echo "Running tests..."
	# Add your test commands here, e.g., ./run_tests

# Clean up generated files
clean:
	rm -f $(OBJECTS) $(TARGET)

# Declare phony targets
.PHONY: build test clean