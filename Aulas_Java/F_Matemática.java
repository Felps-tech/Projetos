package Aulas_Java;

public class F_Matemática {
    public static void main(String[] args){
        //-Aula 7 Matemática-
         
        //-Math.max(x,y)-
        Math.max(5, 10); // 10
        
        //-Math.min(x,y)-
        Math.min(5, 10); // 5
        
        //-Math.sqrt(x)-
        Math.sqrt(64); // 8
        
        //-Math.abs(x)-
        Math.abs(-4.7); // 4.7
        
        //-Math.random()-
        //Retorna um valor de 0.0(inclusivo) a 1.0(exclusivo)
        int randomNum = (int)(Math.random() * 101); // 0 to 100
        System.out.println(randomNum);
    }
}
