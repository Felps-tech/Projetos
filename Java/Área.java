package Projetos.Java;

import java.util.Scanner;

public class Área {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final double pi = 3.14159;
        float a, b, c;
        double triangulo, circulo, trapezio, quadrado, retangulo;
        a = sc.nextFloat();
        b = sc.nextFloat();
        c = sc.nextFloat();
        triangulo = (a * c) / 2;
        circulo = pi * c * c;
        trapezio = (a + b) / 2 * c;
        quadrado = b * b;
        retangulo = a * b;
        System.out.printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n",triangulo,circulo,trapezio,quadrado,retangulo);
        sc.close();
    }
}
