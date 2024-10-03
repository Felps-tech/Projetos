package Projetos.Java;

import java.util.Scanner;

public class ExtremamenteBásico {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num1, num2;

        num1 = scan.nextInt();
        num2 = scan.nextInt();

        int soma = num1 + num2;
        System.out.println("X = " + soma);
        scan.close();
    }

}
