package Aulas_Java;

public class B_Variáveis {
    public static void main(String[] args) {
        //-Aula 2 Usos das variáveis
        
        //-Manipulando variáveis
        String nome = "Felipe";
        System.out.println(nome);
        
        //-Concatenar string
        String prinome = "Felipe ";
        String segnome = "Angélico";
        String nomeint = prinome + segnome;
        System.out.println(nomeint);
        
        //-Com números tambem-
        int x = 5;
        int y = 6;
        System.out.print(x + y);
        
        //-Definir varias variáveis ao mesmo tempo-
        
        int a = 5;
        int b = 6;
        int c = 50;
        //BOZO LOL
        System.out.println(a + b + c);
        
        int d = 5, e = 6, f = 50;
        System.out.println(d + e + f);
        
        int g,h,i;
        g = h = i = 50;
        System.out.println(g + h + i);
    }
}
