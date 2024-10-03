package Projetos.Java;

import java.util.Scanner;

public class Maior {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        int maior = maior(a, b, c);
        System.out.println(maior + " eh o maior");
        sc.close();
    }
        public static int maior(int x, int y, int z){
            x = Math.max(x, y);
            return Math.max(z, x);

    }
}
