package Projetos.Java;

import java.util.Scanner;

public class TesteSeleção {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c, d;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        if (b > c && d > a && (c + d) > (b + a) && c > 0 && d > 0 && a % 2 == 0) {
            System.out.print("Valores aceitos");
        } else {
            System.out.print("Valores nao aceitos");
        }
        sc.close();
    }
}
