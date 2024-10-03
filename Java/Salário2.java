package Projetos.Java;

import java.util.Scanner;

public class Salário2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nome;
        double salario_fixo, vendas;
        nome = sc.nextLine();
        salario_fixo = sc.nextDouble();
        vendas = sc.nextDouble();
        nome.toUpperCase();
        System.out.printf("TOTAL VENDAS DE %s= R$ %.2f\n", nome, vendas * 0.15 + salario_fixo);
        sc.close();
    }
}
