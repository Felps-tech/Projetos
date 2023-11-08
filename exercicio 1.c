#include <stdio.h>
#include <string.h>

int main(){
    char s[100] = {};
    char letra1;
    char letra2;

    while (scanf("%[^'\n']s", s) != EOF){
        getchar();
        scanf("%c %c", &letra1, &letra2);
            printf("String original: %s\n", s);
                int comprimento = strlen(s);
                    for (int i = 0; i < comprimento; i++){
                        if(s[i] == letra1){
                            s[i] = letra2;
                        }

                    }
         printf("String modificada: %s\n", s);
         s[0] = '\0';
        getchar();
    }
    
    return 0;
}
