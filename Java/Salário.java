package Projetos.Java;

import java.util.Scanner;

public class Salário {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, horas;
        float salario_hora, salario;
        numero = sc.nextInt();
        horas = sc.nextInt();
        salario_hora = sc.nextFloat();

        salario = horas * salario_hora;

        System.out.println("NUMBER = " + numero);
        System.out.printf("SALARY = U$ %.2f\n", salario);
        sc.close();
    }

}
