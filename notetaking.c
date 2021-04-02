#include <stdio.h>
#include <stdlib.h>


int main() {
    int input_check = 1;
    char writing[] = {};
    int index = 0;
    while (input_check == 1) {
        input_check = scanf("%c", &writing);
        index++;
        if (writing[index] == '-') {
            printf("beans");

        }

    }
    return 0;

}