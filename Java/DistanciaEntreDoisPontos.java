package Projetos.Java;

import java.util.Scanner;

public class DistanciaEntreDoisPontos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float x1, y1, x2, y2, distancia;
        x1 = sc.nextFloat();
        y1 = sc.nextFloat();
        x2 = sc.nextFloat();
        y2 = sc.nextFloat();
        distancia = (float) Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        System.out.printf("%.4f\n", distancia);
        sc.close();
    }
}
