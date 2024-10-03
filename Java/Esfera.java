package Projetos.Java;

import java.util.Scanner;

public class Esfera {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final double pi = 3.14159;
        int raio = sc.nextInt();
        double volume = 4.0 / 3 * pi * raio * raio * raio;
        System.out.printf("VOLUME = %.3f", volume);
        sc.close();
    }
}
