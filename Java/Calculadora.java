package Projetos.Java;
import java.util.Scanner;
public class Calculadora {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Escolha sua opção da calculadora \n 1:+ \n 2:- \n 3:* \n 4:/");
    int a;
    float b,c;
    a = sc.nextInt();
    System.out.println("Escreva o primeiro numero em formato float(1,0)");
    b = sc.nextFloat();
    System.out.println("Escreva o segundo numero em formato float(1,0)");
    c = sc.nextFloat(); 
    sc.close();
    switch (a) {
        case 1:
        System.out.println("A resposta é: "+(float)(b+c));
        break;
        case 2:
        System.out.println("A resposta é: "+(float)(b-c));
        break;
        case 3:
        System.out.println("A resposta é: "+(float)(b*c));
        break;
        case 4:
        if(c == 0)
        System.out.println("A resposta é indefinida ");
        else
        System.out.println("A resposta é: "+ (float)(b/c));
        default:
        }
    }
}