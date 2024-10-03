package Projetos.Java;

import java.util.*;

public class IdadeEmDias {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dias, anos, meses;
        anos = meses = 0;
        dias = sc.nextInt();
        while (dias >= 365) {
            dias -= 365;
            anos++;
        }
        while (dias >= 30) {
            dias -= 30;
            meses++;
        }
        System.out.printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", anos, meses, dias);
        sc.close();
    }
}