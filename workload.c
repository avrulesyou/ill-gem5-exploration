#include <stdio.h>

// A simple program with a loop to serve as a benchmark for ILP techniques.
// The volatile keyword is used to prevent the compiler from optimizing
// the loop away, ensuring the instructions are actually executed.

int main() {
    volatile int a = 0;
    for (int i = 0; i < 100; i++) {
        a += i;
    }
    printf("Final value: %d\n", a);
    return 0;
}
