package Aulas_Java;

public class A_Introdução {
    public  static void main(String[] args) {
        //Aula 1 Variáveis e prints
         
        int inteiro = 1; // int igual como sempre
        float flutuante = 1.5f; // float sempre com o f após o número
        String frase = "Frase"; // string sempre com aspas duplas
        char caracter = 'A'; // char sempre com aspas simples
        boolean booleano = true; // boolean sempre minúsculo
        
        //-Final-
        //Torna o valor em constante e imutavel
        //final int Num = 2; Este valor não pode ser alterado
        
        System.out.println(inteiro);
        System.out.println(flutuante);
        System.out.println(frase);
        System.out.println(caracter);
        System.out.println(booleano);
        
        //-Alterando os valores das variáveis-
        inteiro = 2;
        flutuante = 2.2f;
        frase = "Outra Frase";
        caracter = 'B';
        booleano = false;
        System.out.println(inteiro);
        System.out.println(flutuante);
        System.out.println(frase);
        System.out.println(caracter);
        System.out.println(booleano);
        
    }
}
