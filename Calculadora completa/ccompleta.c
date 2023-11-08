#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(void)
{

    float num1 = 0,
          num2 = 0,
          num3 = 0,
          num4 = 0,
          num5 = 0,
          delta,
          pi = 3.14,
          r1,
          r2,
          media,
          arcsen,
          arccos,
          arctan,
          area = 0;
    int oper = 0,
        opercc = 0,
        operct = 0,
        operccc = 0,
        dividendo = 2;
    do
    {
        printf("Digite o tipo de calculadora que deseja utilizar\n");
        printf("'1': calculadora basica\n");
        printf("'2': calculadora circulos\n");
        printf("'3': calculadora triangulo\n");
        printf("'4': leitor de valor numero\n");
        printf("\nDigite '0' para fechar a calculadora\n");
        scanf("%d", &oper);

        system("cls || clear");
        
        switch (oper)
        {
        case 1:
            do
            {
                printf("***Calculadora***\n");

                printf("\nOperacoes disponiveis\n");
                printf("'1' : soma\n");
                printf("'2' : subtracao\n");
                printf("'3' : multiplicao\n");
                printf("'4' : divisao\n");
                printf("'5' : raiz quadrada\n");
                printf("'6' : potencia\n");
                printf("'7' : bhaskara\n");
                printf("'8' : media aritmetica\n");
                printf("'0' : sair\n");
                scanf("%d", &opercc);
                system("cls || clear");

                switch (opercc)
                {
                case 1:
                    printf("Digite o primeiro numero:\n");
                    scanf("%f", &num1);
                    printf("Digite o segundo numero:\n");
                    scanf("%f", &num2);
                    system("cls || clear");
                    printf("Calculando %.f + %.f: %.2f\n\n", num1, num2, num1 + num2);
                    break;

                case 2:
                    printf("Digite o primeiro numero:\n");
                    scanf("%f", &num1);
                    printf("Digite o segundo numero:\n");
                    scanf("%f", &num2);
                    system("cls || clear");
                    printf("Calculando %.f - %.f: %.2f\n\n", num1, num2, num1 - num2);
                    break;

                case 3:
                    printf("Digite o primeiro numero:\n");
                    scanf("%f", &num1);
                    printf("Digite o segundo numero:\n");
                    scanf("%f", &num2);
                    system("cls || clear");
                    printf("Calculando %.f * %.f: %.2f\n\n", num1, num2, num1 * num2);
                    break;

                case 4:
                    printf("Digite o primeiro numero:\n");
                    scanf("%f", &num1);
                    printf("Digite o segundo numero:\n");
                    scanf("%f", &num2);
                    system("cls || clear");
                    if (num2 != 0)
                        printf("Calculando %.f / %.f: %.2f\n\n", num1, num2, num1 / num2);
                    else
                        printf("Nao existe divisao por 0\n\n");
                    break;
                case 5:
                    printf("Digite o numero:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando %.f^1/2: %.2f\n\n", num1, sqrt(num1));
                    break;

                case 6:
                    printf("Digite o primeiro numero:\n");
                    scanf("%f", &num1);
                    printf("Digite o segundo numero:\n");
                    scanf("%f", &num2);
                    system("cls || clear");
                    printf("Calculando %.f^%.f: %.2f\n\n", num1, num2, pow(num1, num2));
                    break;
                case 7:
                    printf("Digite o valor de 'a':\n");
                    printf("'?'x^2 +- bx +- c = 0\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Digite o valor de 'b':\n");
                    printf("%.0fx^2 +- '?'x +- c = 0\n", num1);
                    scanf("%f", &num2);
                    system("cls || clear");
                    printf("Digite o valor de 'c\n");
                    if (num2 >= 0)
                    {
                        printf("%.0fx^2 + %.0fx +- '?' = 0\n", num1, num2);
                    }
                    else
                        printf("%.0fx^2 %.0fx +- '?' = 0\n", num1, num2);
                    scanf("%f", &num3);
                    system("cls || clear");
                    delta = (num2 * num2) - (4 * num1 * num3);
                    r1 = ((-num2) + (sqrt(delta))) / (2 * num1);
                    r2 = ((-num2) - (sqrt(delta))) / (2 * num1);
                    if (delta <= 0 || num1 == 0 || num2 == 0 || num3 == 0)
                    {
                        printf("Impossivel calcular\n");
                    }
                    else if (num3 >= 0 && num2 >= 0)
                    {
                        printf("Raiz 1 para a funcao %.0fx^2 + %.0fx + %.0f = 0 = %.2lf\n", num1, num2, num3, r1);
                        printf("Raiz 2 para a funcao %.0fx^2 + %.0fx + %.0f = 0 = %.2lf\n", num1, num2, num3, r2);
                    }
                    else if (num3 < 0 && num2 >= 0)
                    {
                        printf("Raiz 1 para a funcao %.0fx^2 + %.0fx % 1.0f = 0 = %.2lf\n", num1, num2, num3, r1);
                        printf("Raiz 2 para a funcao %.0fx^2 + %.0fx % 1.0f = 0 = %.2lf\n", num1, num2, num3, r2);
                    }
                    else if (num3 >= 0 && num2 < 0)
                    {
                        printf("Raiz 1 para a funcao %.0fx^2 % 1.0fx + %.0f = 0 = %.2lf\n", num1, num2, num3, r1);
                        printf("Raiz 2 para a funcao %.0fx^2 % 1.0fx + %.0f = 0 = %.2lf\n", num1, num2, num3, r2);
                    }
                    break;
                case 8:
                    printf("Digite o primeiro valor\n");
                    scanf("%f", &num1);
                    printf("Digite o segundo valor\n");
                    scanf("%f", &num2);
                    printf("Digite o valor da media\n");
                    scanf("%f", &media);
                    system("cls || clear");
                    num3 = (num1 + num2) / 2;
                    printf("A media aritmetica: (%.f + %.f)/2 = %.2f\n", num1, num2, num3);
                    printf("Media: %.f\n", media);
                    if (media <= num3)
                    {
                        printf("Aprovado\n");
                    }
                    else if (media > num3)
                        printf("Reprovado\n");
                    break;
                default:
                    if (oper != 0 && oper != 1 && oper != 2 && oper != 3 && oper != 4 && oper != 5 && oper != 6 && oper != 7)
                    {
                        printf("Digite uma numero valida\n\n");
                    }
                    break;
                }

            } while (opercc != 0);
            break;
        case 2:
            do
            {
                printf("***Calculadora para Circunferencias***\n");
                printf("\nEscolha a funcao que deseja utilizar\n");
                printf("'1': area do circulo\n");
                printf("'2': circunferencia\n");
                printf("'0': sair\n");

                scanf("%d", &operccc);
                system("cls || clear");

                switch (operccc)
                {
                case 1:
                    printf("Digite o raio:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando pi * %.f^2 :%.2f\n\n", num1, pi * num1 * num1);
                    break;

                case 2:
                    printf("Digite o raio\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando 2 * pi * %.f:%.2fv\n\n", num1, 2 * pi * num1);
                    break;

                default:
                    if (operccc != 0 && operccc != 1 && operccc != 2)
                        printf(" Operador invalido\n\n ");

                    break;
                }

            } while (operccc != 0);
            break;
        case 3:
            do
            {
                printf("***Calculadora para Triangulos***\n");
                printf("\nEscolha a funcao que deseja utilizar\n");
                printf("'1' : area do triangulo\n");
                printf("'2' : seno\n");
                printf("'3' : cosseno\n");
                printf("'4' : tangente\n");
                printf("'5' : seno inverso\n");
                printf("'6' : cosseno inverso\n");
                printf("'7' : tangente inversa\n");
                printf("'8' : angulo do seno\n");
                printf("'9' : angulo do cosseno\n");
                printf("'10': angulo da tangente\n");
                printf("'0' : sair\n");

                scanf("%d", &operct);
                system("cls || clear");

                switch (operct)
                {
                case 1:
                    printf("Digite a base\n");
                    scanf("%f", &num1);
                    printf("Digite a altura\n");
                    scanf("%f", &num2);
                    system("cls || clear");
                    area = (num1 * num2) / 2;
                    printf("Area do triangulo (%.f * %.f)/2: %.1f\n", num1, num2, area);
                    break;

                case 2:
                    printf("Digite o angulo:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando seno %.f: %.2f\n\n", num1, sinf((num1 * pi) / 180));
                    break;

                case 3:
                    printf("Digite o angulo:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando cosseno %.f: %.2f\n\n", num1, cosf((num1 * pi) / 180));
                    break;

                case 4:
                    printf("Digite o angulo:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando tangente %.f: %.2f\n\n", num1, tanf((num1 * pi) / 180));
                    break;

                case 5:
                    printf("Digite o angulo:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando seno inverso %.f: %.2f\n\n", num1, 1 / sinf((num1 * pi) / 180));
                    break;

                case 6:
                    printf("Digite o angulo:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    printf("Calculando cosseno inverso %.f: %.2f\n\n", num1, 1 / cosf((num1 * pi) / 180));
                    break;

                case 7:
                    printf("Digite o angulo:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    if (num1 != 180 && num1 != 360 && num1 != 0)
                        printf("Calculando tangente inversa %.f: %.2f\n\n", num1, 1 / tanf((num1 * pi) / 180));
                    else
                        printf("Nao existe valor de tangente nessa caso\n");
                    break;

                case 8:
                    printf("Digite o valor do seno:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    arcsen = (180 * asin(num1)) / pi;
                    printf("Calculando o angulo para seno valendo %.2f: %.2f\n\n", num1, arcsen);

                    break;

                case 9:
                    printf("Digite o valor do cosseno:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    arccos = (180 * acos(num1)) / pi;
                    printf("Calculando o angulo para cosseno valendo %.2f: %.2f\n\n", num1, arccos);

                    break;

                case 10:
                    printf("Digite o valor da tangente:\n");
                    scanf("%f", &num1);
                    system("cls || clear");
                    arctan = (180 * atan(num1)) / pi;
                    printf("Calculando o angulo para tangente valendo %.2f: %.2f\n\n", num1, arctan);

                    break;

                default:
                    if (oper != 0 && oper != 1 && oper != 2 && oper != 3 && oper != 4 && oper != 5 && oper != 6 && oper != 7 && oper != 8 && oper != 9 && oper != 10)
                    {

                        printf("Digite uma letra valida\n\n");
                    }
                    break;
                }
            } while (operct != 0);
            break;
        }
    } while (oper != 0);
}