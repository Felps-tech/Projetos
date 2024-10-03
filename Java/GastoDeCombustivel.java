package Projetos.Java;

import java.util.Scanner;

public class GastoDeCombustivel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int velocidade = sc.nextInt();
        int horas = sc.nextInt();
        System.out.printf("%.3f", horas*velocidade/12.0);
        sc.close();
    }
}
