#include <stdio.h>
int main()
{
    int x;

    while (scanf("%d", &x) && (x))
    {
        int totalinha = (x * 2) - 1;
        int valor1 = 0;
        int valor2 = 1;
        int valor3;
        for (int j = 1; j <= totalinha; j++)
        {
            if (j <= x)
            {
                for (int i = 1; i <= j; i++)
                {
                    if (i <= 1)
                    {
                        valor3 = i;
                    }
                    else
                    {
                        valor3 = valor1 + valor2;
                        valor1 = valor2;
                        valor2 = valor3;
                    }
                    printf("%d ", valor3);
                }
                valor1 = 0;
                valor2 = 1;
                puts("\n");
            }
            else
            {   
                valor1 = 1;
                valor2 = 0;
                for (int i = j; i <= totalinha; i++)
                {
                 
                        valor3 = valor1 + valor2;
                        valor1 = valor2;
                        valor2 = valor3;
            
                    printf("%d ", valor3);
                }
                
                puts("\n");
            }
        }
    }
    return 0;
}