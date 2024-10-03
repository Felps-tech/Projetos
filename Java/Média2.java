package Projetos.Java;

import java.util.Scanner;

public class Média2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x,y,z, media;
        x = sc.nextDouble();
        y = sc.nextDouble();
        z = sc.nextDouble();
        media = ((x * 2) + (y * 3) + (z * 5))/10;
        System.out.printf("MEDIA = %.1f\n", media);
        sc.close();
    }
}