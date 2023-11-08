#include <stdio.h>

int main() {
    int n = 5;  // Número de linhas desejado
    int a = 1, b = 1;  // Inicialização dos dois primeiros números da sequência

    for (int i = n; i > 0; ) { // n=4 linhas=7 j=5 i=5
        for (int j = 0; j < i; j++) {
            printf("%d ", a);
            int next = a + b;
            a = b;
            b = next;
        }
        printf("\n");
        a = 1;
        b = 1;
        i--;
    }

    return 0;
}
