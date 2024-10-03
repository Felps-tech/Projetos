package Projetos.Java;

import java.util.Scanner;

public class Diferença {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, y, z, w, Diferença;
        x = sc.nextInt();
        y = sc.nextInt();
        z = sc.nextInt();
        w = sc.nextInt();
        Diferença = (x * y - z * w);
        System.out.println("DIFERENCA = " + Diferença);
        sc.close();
    }
}