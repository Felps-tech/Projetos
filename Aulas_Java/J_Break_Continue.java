package Aulas_Java;

public class J_Break_Continue {
    public static void main(String[] args){
        //-Aula 13 Break and Continue-
        
        //-Break-
        for (int i = 0; i < 10; i++) {
        if (i == 4) {
        break;
        }
        System.out.println(i);
        }
        
        //-Continue-
        for (int i = 0; i < 10; i++) {
        if (i == 4) {
        continue;
        }
        System.out.println(i);
        }
    }
}