package Projetos.Java;

import java.util.Scanner;

public class Soma {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println("SOMA = " + (x + y));
        sc.close();
    }
}
