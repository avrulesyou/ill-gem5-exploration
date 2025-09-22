#include <stdio.h>

// A second, slightly different workload for the SMT simulation.
// It runs for a longer duration to better demonstrate how threads
// can share resources.

int main() {
    volatile int a = 0;
    // Loop to 200 instead of 100
    for (int i = 0; i < 200; i++) {
        a += i;
    }
    printf("Final value: %d\n", a);
    return 0;
}
