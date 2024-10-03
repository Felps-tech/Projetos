package Projetos.Java;

import java.util.Scanner;

public class Calculo_Simples {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float dinheiro;
        int cem, cinquenta, vinte, dez, cinco, dois, um, mcinquenta, mvintecinco, mdez, mcinco;
        cem = cinquenta = vinte = dez = cinco = dois = um = mcinquenta = mvintecinco = mdez = mcinco = 0;
        dinheiro = sc.nextFloat();
        cem = (int) dinheiro / 100;
        dinheiro = (float) dinheiro % 100;
        cinquenta = (int) dinheiro / 50;
        dinheiro = (float) dinheiro % 50;
        vinte = (int) dinheiro / 20;
        dinheiro = (float) dinheiro % 20;
        dez = (int) dinheiro / 10;
        dinheiro = (float) dinheiro % 10;
        cinco = (int) dinheiro / 5;
        dinheiro = (float) dinheiro % 5;
        dois = (int) dinheiro / 2;
        dinheiro = (float) dinheiro % 2;
        um = (int) dinheiro;
        dinheiro = (float) dinheiro % 1;
        dinheiro *= 100;
        mcinquenta = (int) dinheiro / 50;
        dinheiro = (float) dinheiro % 50;
        mvintecinco = (int) dinheiro / 25;
        dinheiro = (float) dinheiro % 25;
        mdez = (int) dinheiro / 10;
        dinheiro = (float) dinheiro % 10;
        mcinco = (int) dinheiro / 5;
        dinheiro = (float) dinheiro % 5;
        

        System.out.println("NOTAS:");
        System.out.printf(
                "%d nota(s) de R$ 100.00\n%d nota(s) de R$ 50.00\n%d nota(s) de R$ 20.00\n%d nota(s) de R$ 10.00\n%d nota(s) de R$ 5.00\n%d nota(s) de R$ 2.00\n",
                cem, cinquenta, vinte, dez, cinco, dois);
        System.out.println("MOEDAS:");
        System.out.printf(
                "%d moeda(s) de R$ 1.00\n%d moeda(s) de R$ 0.50\n%d moeda(s) de R$ 0.25\n%d moeda(s) de R$ 0.10\n%d moeda(s) de R$ 0.05\n%.0f moeda(s) de R$ 0.01\n",
                um, mcinquenta, mvintecinco, mdez, mcinco, dinheiro);
        sc.close();
    }
}
