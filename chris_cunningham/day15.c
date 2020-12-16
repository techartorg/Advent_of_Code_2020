#include <stdio.h>
#include <stdlib.h>

const u_int32_t inputs[6] = {15, 12, 0, 14, 3, 1};
const size_t inputs_len = 6;

const u_int32_t countA = 2020;
const u_int32_t countB = 30000000;

int main() {
    u_int32_t last = inputs[inputs_len - 1];

    u_int32_t *seen = (u_int32_t *) malloc(countB * sizeof(u_int32_t));
    for (u_int32_t i = 0; i < inputs_len; i++) {
        seen[inputs[i]] = i + 1;
    }

    for (u_int32_t i = inputs_len; i < countB; i++) {
        u_int32_t j = seen[last];
        seen[last] = i;

        if (i == countA) {
            printf("part a: %d\n", last);
        }

        if (j == 0) {
            last = 0;
        } else {
            last = i - j;
        }
    }
    free(seen);

    printf("part b: %d\n", last);

    return 0;
}
