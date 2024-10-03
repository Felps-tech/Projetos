package Projetos.Java;

import java.util.Scanner;

public class Distancia {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int distancia = sc.nextInt();
        System.out.printf("%d minutos\n", distancia * 2);
        sc.close();
    }
}
