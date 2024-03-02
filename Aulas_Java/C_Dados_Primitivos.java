package Aulas_Java;

public class C_Dados_Primitivos {
    public static void main(String[] args) {
        // -Aula 3 Tipos de dados primitivos-

        // byte | 1 byte | Armazena números inteiros de -128 até 127
        // short | 4 bytes | Armazena números inteiros de -2,147,483,648 até
        // 2,147,483,647
        // long | 8 bytes | Armazena números inteiros de -9,223,372,036,854,775,808 até
        // 9,223,372,036,854,775,807
        // float | 4 bytes | Armazena números fracionados Suficiente para 6 a 7 dígitos
        // double | 8 bytes | Armazena números fracionados Suficiente para 15 dígitos
        // boolean | 1 bit | Armazena true ou false
        // char | 2 bytes | Armazena uma unica letra ou valor ASCII

        //%s String
        //%d Inteiro Decimal
        //%u Inteiro Decimal sem sinal
        //%o Inteiro Octal sem sinal
        //%x, %X Inteiro hexadecimal sem sinal, minusculo ou maiusculo
        //%f Float
        //%2f Double
        //%e, %E Real, Notação científica com um "e" minúsculo ou maiúsculo
        //%b Boolean
        //%c Caractere único

        // -Coisas a notar-
        long Longo = 10000000L; // long usa um L para indicar que é do tipo long
        double Dobro = 20000.32d; // double usa um D para indicar que é do tipo double
        System.out.print(Longo);
        System.out.print(Dobro);
        // Alem dessa mudança esses falores podem usar o e para mostrar numeros
        // cientifico
        float f1 = 35e3f;
        double d1 = 12E4d;
        System.out.println(f1);
        System.out.println(d1);

        // Aula 4 Conversão de tipos

        // -Ordem de Alargar-
        // byte -> short -> int -> long -> float -> double (ele faz automaticamente)
        // Ordem de Reduzir
        // byte <- short <- int <- long <- float <- double (deve ser feito manualmente)

        // -Exemplos-

        int MyInt = 5;
        float MyFloat = MyInt; // Alargar automaticamente
        System.out.println(MyFloat);

        float MyFloat2 = 5.5f;
        int MyInt2 = (int) MyFloat2; // Reduzir manualmente
        System.out.println(MyInt2);
    }
}