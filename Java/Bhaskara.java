package Projetos.Java;

import java.util.*;

public class Bhaskara {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a, b, c, delta;
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();
        delta = (b*b)-(4*a*c);
        
        if (delta < 0 || a == 0){
            System.out.println("Impossivel calcular");
        }
        else{
            double x1 = (-b + Math.sqrt(delta)) / (2 * a);
            double x2 = (-b - Math.sqrt(delta)) / (2 * a);
            
            System.out.printf("R1 = %.5f\nR2 = %.5f",x1,x2);
        }
        sc.close();
    }
}
