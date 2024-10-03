package Projetos.Java;

import java.util.Scanner;

public class Cédulas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int notas, cem, cinquenta, vinte, dez, cinco, dois;
        cem = cinquenta = vinte = dez = cinco = dois = 0;
        notas = sc.nextInt();
        System.out.println(notas);
        while (notas >= 100) {
            notas -= 100;
            cem++;
        }
        while (notas >= 50) {
            notas -= 50;
            cinquenta++;
        }
        while (notas >= 20) {
            notas -= 20;
            vinte++;
        }
        while (notas >= 10) {
            notas -= 10;
            dez++;

        }
        while (notas >= 5) {
            notas -= 5;
            cinco++;
        }
        while (notas >= 2) {
            notas -= 2;
            dois++;
        }
        System.out.printf("%d nota(s) de R$ 100,00\n",cem);
        System.out.printf("%d nota(s) de R$ 50,00\n",cinquenta);
        System.out.printf("%d nota(s) de R$ 20,00\n",vinte);
        System.out.printf("%d nota(s) de R$ 10,00\n",dez);
        System.out.printf("%d nota(s) de R$ 5,00\n",cinco);
        System.out.printf("%d nota(s) de R$ 2,00\n",dois);
        System.out.printf("%d nota(s) de R$ 1,00\n",notas);
        sc.close();
    }
}