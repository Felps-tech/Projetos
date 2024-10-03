package Projetos.Java;

import java.util.Scanner;

public class Consumo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int km; 
        float litros;
        km = sc.nextInt();
        litros = sc.nextFloat();
        System.out.printf("%.3f km/l\n", km/litros);
        sc.close();
    }
}
