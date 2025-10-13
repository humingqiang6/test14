.section .text
.global asm_add

# Function: asm_add
# Parameters: int a (in %rdi), int b (in %rsi)
# Returns:  a + b (in %rax)
asm_add:
    movq    %rdi, %rax  # Copy the first argument (a) to %rax
    addq    %rsi, %rax  # Add the second argument (b) to %rax
    ret                 # Return the result in %rax
