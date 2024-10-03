package Projetos.Java;

import java.util.Scanner;

public class CédulasEMoedas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero1, numero2, quant1, quant2;
        float valor1, valor2;
        numero1 = sc.nextInt();
        quant1 = sc.nextInt();
        valor1 = sc.nextFloat();
        numero2 = sc.nextInt();
        quant2 = sc.nextInt();
        valor2 = sc.nextFloat();
        System.out.printf("VALOR A PAGAR DOS PEDIDOS %s E %s: R$ %.2f",numero1,numero2, (quant1 * valor1) + (quant2 * valor2));
        sc.close();
    }
}
